pipeline {
    agent any

    stages {
        stage('Deploy Applications using Ansible') {
            steps {
                echo 'Starting application deployment'

                withCredentials([
                    string(
                        credentialsId: 'vm-sudo-password',
                        variable: 'VM_SUDO_PASSWORD'
                    )
                ]) {
                    sh '''
                        set +x

                        printf '%s\\n' "$VM_SUDO_PASSWORD" | \
                        ssh meghamurali@172.17.0.1 '
                            cd ~/applications-ansible &&
                            git pull origin main &&
                            umask 077 &&
                            pwfile=$(mktemp) &&
                            cat > "$pwfile"

                            ansible-playbook \
                                -i inventory/hosts.ini \
                                site.yml \
                                --become-password-file="$pwfile"

                            result=$?
                            rm -f "$pwfile"
                            exit "$result"
                        '
                    '''
                }
            }
        }
    }
}
