pipeline {
    agent {
        label 'test'
    }
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = 'kerenmal/WorldOfGames'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                script {
                    bat 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    bat 'docker-compose up -d'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'python e2e.py'
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    bat 'docker-compose down'
                    bat 'echo %DOCKERHUB_CREDENTIALS_PSW% | docker login -u %DOCKERHUB_CREDENTIALS_USR% --password-stdin'
                    bat 'docker push %IMAGE_NAME%'
                }
            }
        }
    }

    post {
        always {
            script {
                bat 'docker system prune -f'
            }
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
