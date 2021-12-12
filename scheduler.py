import yaml
import urllib3, requests, json
import time
import sys

def triggerTestPlanForNode(plan):
    url = "http://localhost:8080/job/ExecuteTestPlanOnNode/buildWithParameters?token=123&node="+plan
    # crumb = requests.get('http://admin:11e0772e9d1cad5a2f19a12bf14b78b714@localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')

    params = {"parameter": [
        {"name": plan+".yaml", "file": "FILE"},
        ]}
    with open(plan+".yaml", "rb") as f:
        file_data = f.read()
    data, content_type = urllib3.encode_multipart_formdata([
        ("FILE", (f.name, file_data)),
        ("json", json.dumps(params)),
        ("Submit", "Build"),
        ])

    resp = requests.post(url, auth=("admin", "11e0772e9d1cad5a2f19a12bf14b78b714"), data=data,
            headers={"content-type": content_type,"Jenkins-Crumb":"2616f44971436bbfb253edceed81d4136d632206dcb5389478499c3c620140f9"}, verify=False)
    print("Triggered Job : "+resp.headers['Location'])
    resp.raise_for_status()

plans_list=[]
# print("Callback URL for scheduler request: "+sys.argv[1])
with open("buildplan.yaml", "r") as stream:
    try:
        plan = yaml.safe_load(stream)
        print("This test plan involves the following nodes:")
        for node in plan["nodes"]:
            print(node['node'][0]['name'] +" : "+node['node'][0]['ip'])
        
            print("Generating isolated test plan for node: "+node['node'][0]['name'])
            with open(node['node'][0]['name']+'.yaml',"w+") as node_plan:
                node_plan.write(yaml.dump(node))
            
            print("isolated plans generated succesfully")
            triggerTestPlanForNode(node['node'][0]['name'])
            time.sleep(10)
    except yaml.YAMLError as exc:
        print(exc)


requests.post(
    url=sys.argv[1],
    data={
        "status":"OK",
    }
)