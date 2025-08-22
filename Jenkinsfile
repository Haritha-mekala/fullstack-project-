pipeline {
    agent { label 'job1' }

    environment {
        COMPOSE_FILE = "docker-compose.yml"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Checking out source code..."
                checkout scm
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "🐳 Building Docker images..."
                sh 'docker-compose build'
            }
        }

        stage('Run Containers') {
            steps {
                echo "🚀 Starting containers with docker-compose..."
                sh 'docker-compose up -d'
            }
        }

        stage('Verify Services') {
            steps {
                echo "🔍 Checking running containers..."
                sh 'docker ps -a'
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful! All services are running."
        }
        failure {
            echo "❌ Deployment failed. Check logs."
        }
    }
}
