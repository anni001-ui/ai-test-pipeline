pipeline {
    agent any

    stages {
        // REMOVED the "Clone" stage because Jenkins does this automatically
        
        stage('Install Dependencies') {
            steps {
                // Using bat for Windows
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
                        error "priority_list.txt not found! Check if ai_prioritization.py is working correctly."
                    }
                }
            }
        }
    }
}
