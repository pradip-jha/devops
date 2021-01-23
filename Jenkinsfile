pipeline {
    agent any
    environment {
    IMAGE_NAME = 'flask-app'
    IMAGE_VERSION = '0.1'
    DOCKER_REPO_NAME = 'pankaj2934'
    DOCKER_CRED = credentials('dockerhub')
    }
    stages {

    stage('docker-login'){
        steps{
            sh '''
            docker login -u $DOCKER_CRED_USR -p $DOCKER_CRED_PSW

            '''
        }
        }
        stage('docker-Build') {
        steps {
            sh '''
            env
            docker build . -t $DOCKER_REPO_NAME/$IMAGE_NAME:$IMAGE_VERSION.$BUILD_NUMBER
            '''
        }
        }
        stage('docker-Push') {
            steps {

            sh '''
            env
            docker push $DOCKER_REPO_NAME/$IMAGE_NAME:$IMAGE_VERSION.$BUILD_NUMBER
            '''

            }
        }
        stage('Update yaml') {
        steps {
            script {
                    echo "updating image version to $IMAGE_VERSION.$BUILD_NUMBER"

                    build propagate: false, job: 'devops-k8', parameters: [string(name: 'Enter_Version_No', value: $IMAGE_VERSION.$BUILD_NUMBER)]
            }
        }
    }
    }
}
