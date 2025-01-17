import base64
import requests
from scrapy.exceptions import DropItem

class CaptchaPipeline:
    def process_item(self, item, spider):
        captcha_url = item.get('captcha_url')
        if not captcha_url:
            return item  # Pas de captcha à résoudre

        api_key = spider.settings.get('CAPTCHA_API_KEY')
        if not api_key:
            spider.logger.error("Aucune API Key pour le service de captcha.")
            raise DropItem("Résolution de captcha impossible")

        # Télécharger l'image captcha
        captcha_response = item.get('captcha_response')
        captcha_image = captcha_response.body
        encoded_image = base64.b64encode(captcha_image).decode('utf-8')

        # Envoyer l'image au service 2Captcha
        response = requests.post(
            'http://2captcha.com/in.php',
            data={'key': api_key, 'method': 'base64', 'body': encoded_image}
        )
        if response.status_code != 200 or 'ERROR' in response.text:
            spider.logger.error(f"Erreur lors de la soumission du captcha: {response.text}")
            raise DropItem("Erreur captcha")

        captcha_id = response.text.split('|')[-1]

        # Obtenir la solution du captcha
        solution_url = f'http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}'
        while True:
            result = requests.get(solution_url)
            if result.text == 'CAPCHA_NOT_READY':
                continue  # Attendre que le captcha soit résolu
            if 'ERROR' in result.text:
                spider.logger.error(f"Erreur de résolution du captcha: {result.text}")
                raise DropItem("Erreur captcha")

            solution = result.text.split('|')[-1]
            spider.logger.info(f"Captcha résolu : {solution}")
            item['captcha_solution'] = solution
            break

        return item
