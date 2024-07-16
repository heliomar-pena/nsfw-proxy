#!/user/bin/env python3.10.14
import subprocess
from mitmproxy import http
from mitmproxy import ctx
import tempfile
import json

def checkNSFWPredictions(predictions):
   isSafe = False;
   for prediction in predictions:
      if (isSafe == False):
        category = prediction['category']
        if (category == 'hentai' or category == 'porn' or category == 'sexy'):
           isSafe = prediction['probability'] > 0.1
      else:
        break
   return isSafe

class NSFWDetector:
    def load(self, loader):
        loader.add_option(
          name="command",
          typespec=str,
          help="You will want that this command run when we wanted to classify image with IA. It should include <dir>.",
          default=""
        )

    def response(self, flow: http.HTTPFlow) -> None:
        if (flow.response.headers.get("Content-Type", "").startswith("image")):
            with tempfile.NamedTemporaryFile(delete_on_close=True,delete=True) as tempFile:
              tempFile.write(flow.response.content);

              command = ctx.options.command.replace('<dir>', tempFile.name);
              commandArr = command.split(' ');
              result = subprocess.run(commandArr, capture_output=True);

              if (result.stderr):
                print("ERROR")
                return

              if (result.stdout):
                 print("SUCCESS")
                 jsonResult = json.loads(result.stdout)

                 print(jsonResult)

                 isNSFW = jsonResult['has_nudity'] == True or checkNSFWPredictions(jsonResult['predictions'])

                 if (isNSFW):
                    blockImage = open('block-image.jpeg', mode='rb').read()
                    flow.response.content = blockImage;
                    flow.response.headers["content-type"] = "image/jpeg"





addons = [NSFWDetector()]