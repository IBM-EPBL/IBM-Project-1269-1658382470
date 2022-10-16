from flask import Flask,redirect,url_for,render_template,request
import ibm_boto3
from ibm_botocore.client import Config, ClientError

COS_ENDPOINT = "https://s3.jp-tok.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "VVULZBQOD2LtqkAPjM7IggmNIWt4Hk55hs9LexMQ0pIT"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:iam-identity::a/10ff59e3de164e4fb4b49193c6cca1df::serviceid:ServiceId-e047fdb4-3ee7-48db-bbe0-52d025487cdf"

cos = ibm_boto3.resource("s3",
    ibm_api_key_id=COS_API_KEY_ID,
    ibm_service_instance_id=COS_INSTANCE_CRN,
    config=Config(signature_version="oauth"),
    endpoint_url=COS_ENDPOINT
)
app=Flask(__name__)

def get_bucket_contents(bucket_name):
    print("Retrieving bucket contents from: {0}".format(bucket_name))
    try:
        files = cos.Bucket(bucket_name).objects.all()
        files_names = []
        for file in files:
            files_names.append(file.key)
            print("Item: {0} ({1} bytes).".format(file.key, file.size))
        return files_names
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
    except Exception as e:
        print("Unable to retrieve bucket contents: {0}".format(e))
@app.route('/')
def index():
    files = get_bucket_contents('prediksha-sg')
    
    return render_template('index.html', files = files)

if __name__=='__main__':
    app.run(debug=True)
