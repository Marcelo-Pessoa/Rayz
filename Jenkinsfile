pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Iniciando a compilação e preparação do código fonte...'
                script {
                    // Garantimos a imagem com o ambiente Python correto
                    bat 'docker pull nikolaik/python-nodejs:python3.10-nodejs16-alpine'
                    
                    // Executamos a compilação dos arquivos fonte (.py para .pyc)
                    bat '''
                        docker run --rm \
                        -v "%WORKSPACE%":/workspace \
                        -w /workspace \
                        nikolaik/python-nodejs:python3.10-nodejs16-alpine \
                        sh -c "echo 'Compilando os códigos fonte...' && python -m compileall . "
                    '''
                }
            }
        }

        stage('Testes Unitários') {
            steps {
                echo 'Iniciando o estágio de testes com o código pré-compilado...'
                script {
                    // Executa estritamente os testes unitários em um container limpo
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