pipeline {
    agent any
    stages {
        stage('Preparation') {
            steps {
                echo 'Preparing environment for Artem Yutsevich...'
            }
        }
        stage('Build') {
            steps {
                echo 'Triggering build logic...'
            }
        }
        stage('Results') {
            steps {
                echo 'Pipeline execution complete. Finished: SUCCESS'
            }
        }
    }
}