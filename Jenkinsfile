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
                    echo 'Packaging HTML files...'
                    // Create a tarball with HTML, CSS, and JS files
                    sh 'tar -czf app.tar.gz *.html *.css *.js' // Adjust this based on your file types
                }
            }
        }

        stage('Deploy to Remote Server') {
            steps {
                sshagent(['wasiq']) { // Use Jenkins credentials ID for SSH
                    echo 'Copying tarball to the remote server...'
                    // Copy the tarball to the remote server
                    sh "scp -o StrictHostKeyChecking=no app.tar.gz ubuntu@16.170.226.85:/tmp/"
                }
            }
        }

        stage('Extract and Deploy') {
            steps {
                sshagent(['wasiq']) { // Use Jenkins credentials ID for SSH
                    echo 'Extracting files on the remote server...'
                    // Extract the tarball into /var/www/html/
                    sh """
                    ssh -o StrictHostKeyChecking=no ubuntu@16.171.255.158 'tar -xzf /tmp/app.tar.gz -C /var/www/html/'
                    ssh -o StrictHostKeyChecking=no ubuntu@16.171.255.158 'rm /tmp/app.tar.gz' // Cleanup
                    """
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
