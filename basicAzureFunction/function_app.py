import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="httpexample", auth_level=func.AuthLevel.ANONYMOUS)
def httpexample(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # basic get parameters from url by '?name=&pp='
    name = req.params.get('name')
    pp = req.params.get('pp')
    # get from json
    if not name or not pp:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            pp = req_body.get('pp')

    if name:
        return func.HttpResponse(f"Hello, {name}({pp}). This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )