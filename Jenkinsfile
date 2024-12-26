pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo 'Checking out code from the GitHub repository...'
                    checkout([
                        $class: 'GitSCM',
                        branches: [[name: '*/main']], // Replace 'main' with your branch name if needed
                        userRemoteConfigs: [[
                            url: 'https://github.com/muhammadwasiqkh/apache.git', // Replace with your repository URL
                           
                        ]]
                    ])
                }
            }
        }

        stage('Package') {
            steps {
                script {
                    echo 'Packaging HTML file...'
                    // Create a tarball with the HTML file
                    sh 'tar -czf app.tar.gz *.html'
                }
            }
        }

       stage('Deploy to Remote Server') {
            steps {
               

                    sshagent(['wasiq']) { // Use Jenkins credentials ID for SSH
                        // Copy the HTML package to the remote server
                        sh "scp -o StrictHostKeyChecking=no -r * ubuntu@16.170.226.85:/var/www/html/"

                    }
                
            }
        }
    }

    post {
        success {
            echo 'Deployment completed successfully!'
        }

        failure {
            echo 'Deployment failed. Please check the logs.'
        }
    }
}
