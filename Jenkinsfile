pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/anni001-ui/anni_001.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('AI Prioritization') {
            steps {
                sh 'python ai_prioritization.py'
            }
        }

        stage('Run Tests in Priority Order') {
            steps {
                script {
                    def tests = readFile('priority_list.txt').split("\n")
                    
                    for (test in tests) {
                        if (test) {
                            sh "pytest tests/${test}"
                        }
                    }
                }
            }
        }
    }
}