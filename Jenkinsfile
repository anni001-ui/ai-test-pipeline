pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                // We specify the 'main' branch explicitly here
                git branch: 'main', url: 'https://github.com/anni001-ui/anni_001.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Changed sh to bat for Windows
                bat 'pip install -r requirements.txt'
            }
        }

        stage('AI Prioritization') {
            steps {
                // Changed sh to bat for Windows
                bat 'python ai_prioritization.py'
            }
        }

        stage('Run Tests in Priority Order') {
            steps {
                script {
                    // Check if the file exists first to avoid Groovy errors
                    if (fileExists('priority_list.txt')) {
                        def tests = readFile('priority_list.txt').split("\n")
                        
                        for (test in tests) {
                            if (test.trim()) { 
                                // Changed sh to bat for Windows
                                bat "pytest tests/${test.trim()}"
                            }
                        }
                    } else {
                        error "priority_list.txt not found! Ensure ai_prioritization.py created it."
                    }
                }
            }
        }
    }
}
