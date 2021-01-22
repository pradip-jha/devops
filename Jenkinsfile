pipeline {
    agent any
    environment {
    IMAGE_NAME='flask-app'
    IMAGE_VERSION='0.1'
    DOCKER_REPO_NAME='pankaj2934'
    }
    stages {
        stage('Build') {
        steps {
            sh '''
            env
            docker build . -t ${DOCKER_REPO_NAME}/${IMAGE_NAME}:${IMAGE_VERSION}.${env.BUILD_NUMBER}
            '''

        }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
