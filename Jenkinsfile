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


        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install boto3 pandas scikit-learn joblib
                pip install sagemaker
                '''
            }
        }

        stage('Run SageMaker Training') {
            steps {
                bat '''
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\python.exe -m pip install sagemaker
                venv\\Scripts\\python.exe -m pip install --upgrade pip wheel setuptools
                python -m venv venv                 
                venv\\Scripts\\python.exe -m pip install numpy==1.26.4
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                venv\\Scripts\\python.exe sagemaker_pipeline.py
                echo "Pipeline is created"
                '''
            }
        }
    }
}
