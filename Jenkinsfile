pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ROLE_ARN   = 'arn:aws:iam::084719916966:role/SageMakerExecutionRole'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup AWS Credentials') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws_cred', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    bat '''
                    if not exist %USERPROFILE%\\.aws mkdir %USERPROFILE%\\.aws
                    echo [default] > %USERPROFILE%\\.aws\\credentials
                    echo aws_access_key_id=%AWS_ACCESS_KEY_ID% >> %USERPROFILE%\\.aws\\credentials
                    echo aws_secret_access_key=%AWS_SECRET_ACCESS_KEY% >> %USERPROFILE%\\.aws\\credentials
                    echo region=%AWS_REGION% >> %USERPROFILE%\\.aws\\credentials
                    '''
                }
            }
        }


        stage('Setup Virtual Environment & Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                venv\\Scripts\\python.exe -m pip install --upgrade pip wheel setuptools
                venv\\Scripts\\python.exe -m pip cache purge
                venv\\Scripts\\python.exe -m pip install --no-cache-dir --only-binary=:all: numpy==1.26.4
                venv\\Scripts\\python.exe -m pip install --no-cache-dir --only-binary=:all: scikit-learn==1.5.2 boto3>=1.35.36 sagemaker==2.215.0
                '''
            }
        }

        stage('Verify Python Environment') {
            steps {
                bat '''
                venv\\Scripts\\python.exe -c "import numpy; numpy.show_config(); print('NumPy version:', numpy.__version__)"
                venv\\Scripts\\python.exe -c "import sklearn; print('scikit-learn version:', sklearn.__version__)"
                venv\\Scripts\\python.exe -c "import boto3; print('boto3 version:', boto3.__version__)"
                venv\\Scripts\\python.exe -c "import sagemaker; print('SageMaker version:', sagemaker.__version__)"
                '''
            }
        }

        stage('Run SageMaker Training Pipeline') {
            steps {
                bat '''
                venv\\Scripts\\python.exe sagemaker_pipeline.py
                echo "Pipeline is created successfully"
                '''
            }
        }
    }
}