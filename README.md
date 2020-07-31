# Pylexa
Boilerplate for creating a new Alexa skill with Python.

# How to Use
1. Click the "Use This Template" button in GitHub. Or, clone via SSH
    ```
    git clone git@github.com:irlrobot/pylexa.git YOUR_SKILL_NAME
    ```
    or HTTPS
    ```
    git clone https://github.com/irlrobot/pylexa.git YOUR_SKILL_NAME
    ```
2. Create a new [Python virtual environment]() with `virtualenv venv`.
3. Install dependencies with `pip install -r requirements-dev.txt` and `pip install -r requirements.txt`.
4. Start adding your code in src/ and your tests in tests/.
5. Use /deps for dependencies. I use another tool I created called [alppb]() to build dependencies on Amazon Linux and download the modules locally for inclusion in your deployment to AWS Lambda.
6. Use `build_and_deploy.py` to help deploy to AWS Lambda quickly.

# Alexa Skills Kit References
* [Request and Response Schema](https://developer.amazon.com/docs/custom-skills/request-and-response-json-reference.html)
* [Interaction Model Schema](https://developer.amazon.com/docs/smapi/interaction-model-schema.html)
