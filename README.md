# Serverless Python Dependencies Test

This project was created using the following serverless command:
```bash
npm install -g serverless
serverless create \
  --template aws-python3 \
  --name sls-python-test \
  --path sls-python-test
```

In this example, a python virtual-environment is created as `venv/` on the root folder and is ignored from version control. it also requires the use of the libraries `pyenv`, `pipenv` and `virtualenv`, so that the project can run without depending on computer-specific resources.
```bash
pyenv local # sets the python version to 3.8.X. Install both pyenv and the version if necessary
virtualenv venv -p python # uses the previously set python to create the env
source venv/bin/activate # to activate the local venv. Run it every time you cd into this function
python -V # make sure you are running 3.8.X
deactivate # to deactivate later, or just close the terminal window
pipenv --venv # to check the path to the running venv
```

Install your dependencies using `pipenv`:
```bash
pipenv install # to install what's on the Pipfile.lock
pipenv install 'numpy==1.16' # if you want to add any new lib with a specific version to your Pipfile
pipenv lock -r # to check the list of requirements that will be installed in the Lambda function
```

Install the wrapper to allow `requirements.txt` to be used in the Lambda function:
```bash
sls plugin install -n serverless-python-requirements
```

Notice that these lines have been added to the `serverless.yml` file so that it uses `docker` to generate the requirements, making it even more standard and reducing potential config failures:
```yaml
custom:
  pythonRequirements:
    dockerizePip: true
```

With the dependencies installed and your [AWS profile activated](https://serverless.com/framework/docs/providers/aws/guide/quick-start/) you can deploy your function:
```bash
sls deploy # creates or updates the stack
sls invoke -f hello --log -d '{"foo": "bar"}' # to invoke the function and passing some JSON data
sls remove # deletes all the created resources
```
