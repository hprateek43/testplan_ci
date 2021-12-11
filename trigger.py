import urllib3, requests, json

url = "http://localhost:8080/job/ExecuteTestPlanOnNode/buildWithParameters?token=123"
# crumb = requests.get('http://admin:11e0772e9d1cad5a2f19a12bf14b78b714@localhost:8080/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)')

params = {"parameter": [
    {"name": "buildplan.yaml", "file": "FILE"},
    ]}
with open("buildplan.yaml", "rb") as f:
    file_data = f.read()
data, content_type = urllib3.encode_multipart_formdata([
    ("FILE", (f.name, file_data)),
    ("json", json.dumps(params)),
    ("Submit", "Build"),
    ])

resp = requests.post(url, auth=("admin", "11e0772e9d1cad5a2f19a12bf14b78b714"), data=data,
        headers={"content-type": content_type,"Jenkins-Crumb":"2616f44971436bbfb253edceed81d4136d632206dcb5389478499c3c620140f9"}, verify=False)
resp.raise_for_status()