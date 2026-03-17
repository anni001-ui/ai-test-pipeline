pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('AI Prioritization') {
            steps {
                bat 'python ai_prioritization.py'
            }
        }

        stage('Run Tests in Priority Order') {
            steps {
                script {
                    if (fileExists('priority_list.txt')) {
                        def tests = readFile('priority_list.txt').split("\n")
                        for (test in tests) {
                            if (test.trim()) {
                                bat "pytest tests/${test.trim()}"
                            }
                        }
                    } else {
                        error "priority_list.txt not found!"
                    }
                }
            }
        }
    }

    // The post block must be outside of stages
    post {
        always {
            archiveArtifacts artifacts: 'priority_list.txt', fingerprint: true
            echo "Build complete. AI Priority list has been archived."
        }
    }
}
