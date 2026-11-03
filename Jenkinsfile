pipeline {
    agent { label  'low-capacity' }

    stages {
        stage('Clone Git Repo') { // job 1
            steps {
                git branch: 'main', url: 'https://github.com/pradeepchittimodu/GFG48-Python-FlaskApp.git'
            }
        }
        stage('Install packages & unit test & Lint check') {
            steps {
                sh 'yum install python3-pip -y'
                sh 'pip3 install -r requirements.txt'
                sh 'pytest'
                sh 'flake8'
            }
        }
        stage('build docker image and run container') {
            steps {
                sh '''docker build -t webapp .
                      docker rm -f $(docker ps -aq)
                      docker run -dit -p 80:80 --name web webapp'''
            }
        }
    }
}
