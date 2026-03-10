pipeline{
    agent any
    stages{
        stage('clone repo'){
            steps{
                git url:'https://github.com/santhoshmanoharan04/dev-projects-beg.git', branch: 'main'
            }
        }
        stage('build docker'){
            steps{
                sh'docker build -t dev-proj-beg .'
            }
        }
        stage('stop docker'){
            steps{
                sh 'docker stop devops-container || true'
                sh 'docker rm devops-container || true'
            }
        }
        stage('run docker'){
            steps{
                sh 'docker run -d -p 5050:5000 --name devops-container dev-proj-beg'
            }
        }
    }
}
