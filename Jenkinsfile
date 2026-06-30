pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Preparando o ambiente do projeto...'
                script {
                    bat 'docker pull nikolaik/python-nodejs:python3.10-nodejs16-alpine'
                    
                    // Apenas lista os arquivos ou roda um comando Python válido se necessário
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        nikolaik/python-nodejs:python3.10-nodejs16-alpine \
                        sh -c "echo 'Arquivos no workspace:' && ls -la"
                    '''
                }
            }
        }

        stage('Testes Unitários') {
            steps {
                echo 'Executando os testes integrados do Django...'
                script {
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        nikolaik/python-nodejs:python3.10-nodejs16-alpine \
                        sh -c "python testes_main.py -v"
                    '''
                }
            }
        }
    }
}