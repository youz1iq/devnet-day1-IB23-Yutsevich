# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student
- Name: Yutsevich Artem
- Group: IB-23-5b
- Token: D1-IB-23-5b-28-F543
- Repo: https://github.com/youz1iq/devnet-day1-IB23-Yutsevich
## 2) Evidence checklist (files exist)
### Docker (6.2.7)
- artifacts/day4/docker/sampleapp_curl.txt: Yes
- artifacts/day4/docker/sampleapp_token_proof.txt: Yes
- artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
- artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)
- artifacts/day4/jenkins/jenkins_docker_ps.txt: Yes
- artifacts/day4/jenkins/buildapp_console.txt: Yes
- artifacts/day4/jenkins/testapp_console.txt: Yes
- artifacts/day4/jenkins/pipeline_script.groovy: Yes
- artifacts/day4/jenkins/pipeline_console.txt: Yes
- artifacts/day4/jenkins/jenkins_url.txt: Yes

### Ansible (7.4.8)
- artifacts/day4/ansible/ansible_ping.txt: Yes
- artifacts/day4/ansible/ansible_hello.txt: Yes
- artifacts/day4/ansible/ansible_playbook_install.txt: Yes
- artifacts/day4/ansible/ports_conf_after.txt: Yes
- artifacts/day4/ansible/curl_apache_8081.txt: Yes

### Security (6.5.10)
- artifacts/day4/security/signup_v1.txt: Yes
- artifacts/day4/security/login_v1.txt: Yes
- artifacts/day4/security/signup_v2.txt: Yes
- artifacts/day4/security/login_v2.txt: Yes
- artifacts/day4/security/db_tables.txt: Yes
- artifacts/day4/security/db_user_hash_sample.txt: Yes

## 3) Commands output
```bash
PS F:\devnet-day1-IB23-yutsevich> py src/day4_summary_builder.py
{
  "schema_version": "4.1",
  "generated_utc": "2026-03-13T09:15:32.073241+00:00",
  "student": {
    "token": "D1-IB-23-5b-28-F543",
    "token_hash8": "659f1a7b",
    "name": "Yutsevich Artem",
    "group": "IB-23-5b"
  },
  "checks": {
    "docker_token_in_page": true,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": true
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "ed844e867cc617169b04a3ab196ff4e5eed3c478be3b9849467f4e804555ffed",
    "docker_ps": "51cd32bf7cf482197531b4a43b6059bfd8e75e3eef39837533843d56fc879f0d",
    "docker_build_log": "271f0895feafcd09971435360214c5bdc6a9ff49f9c925e4d53c468257ea150e",
    "docker_token_proof": "112397b8ee8927e28e11b78d17f1e734c9334c9c04b84d8238c9ad9f07fad53f",
    "jenkins_docker_ps": "d576c5d89afbf75f07ac53e6f063b9c6e24a8f26b3e8c4bfefa02145837a33d2",
    "buildapp_console": "a323b49fc0ebaf35295a62e130408592280a87c35f0c78b027a596f37a6a0414",
    "testapp_console": "1f8ed48ff293d03cc9a0f6681c4a4269ba21edc568481cf38aa741586452164d",
    "pipeline_script": "553458a41b992f8c63d267217174e6b8dbd63e4ac5e8241d417e99411a8a5a6a",
    "pipeline_console": "3b8f5a9bd300adde955a6e3aaf5fcd09cf6793b9d49eea87750ae2c347eccdcf",
    "jenkins_url": "116e0500c068cf6a6cd39e9a357eaeb6c40ab688aa4bb15a54d21dc15b3d712c",
    "ansible_ping": "de6ed00cb84798fb16d9a61eaa08bb003219e43f8ce76ba8eb7d4e12166e7dcc",
    "ansible_hello": "4041e39533a37068e57eb8d824c275e4ae7130009e6df32513856332ea316681",
    "ansible_playbook_install": "f5cc3fe6fabf7b3f98d1530ee9d09c757eb3c256394221c6da9d183379b44be8",
    "ports_conf_after": "4ffa53ad3e0877bf9d4ea6f41c3e2a9989456df776af4ce6bc6351fc1d19d686",
    "curl_apache_8081": "4082f2363927a0d653bfe6a70f745637bb06ca6f6baa27f670711dda122c1ac4",
    "signup_v1": "50ac047dc8b610abd66f26a2455ae39ceac12ad1bd5689e8d191242c77c69093",
    "login_v1": "281147ce621ee0f24d0523647763fbc60be98f745ca23ffd8be003f84a6dbd94",
    "signup_v2": "2f0f244f062dd579a4b40e4a41f856ae1b4fce37322c0ccf4d6469804d676377",
    "login_v2": "74243ddc7d88cf2c4a41848d77b1b3b5202a0ccc5b7c2ba541384303f10dda0e",
    "db_tables": "e51666ec716c8164bb8c83993499c29beeb6aaf11f09ba0c0e43dcca23a38e82",
    "db_user_hash_sample": "9b100dbe6bbe3467239095c84aea243ab2f00158e4afb0e259d6751687042d8a"
  },
  "validation_passed": true,
  "run": {
    "python": "3.14.2",
    "platform": "win32"
  }
}
```
```bash
PS F:\devnet-day1-IB23-yutsevich> py -m pytest -q .\tests\test_day4_labs.py        
.                                                                                                                                                                        [100%]
1 passed in 0.12s
```

## 4) Short reflection

Самой сложной частью сегодня была настройка Jenkins Pipeline и обеспечение того, чтобы все инструменты выдавали артефакты в нужном формате для автоматического билдера.Ошибка, которой удалось избежать - хранение паролей в открытом виде в БД; использование хешей в Lab 6.5.10 наглядно показало правильный подход к безопасности.

## 5) Problems & fixes
Problem: При запуске Pipeline в Jenkins возникала ошибка permission denied при попытке выполнить docker build. Это происходило потому, что пользователь jenkins внутри контейнера не имел прав на взаимодействие с Docker-демоном хостовой машины через сокет.

Fix: Добавил пользователя jenkins в группу docker на хосте и пробросил сокет через volume в docker-compose.yaml. Также временно применил chmod 666 /var/run/docker.sock для проверки связи.

Proof: Этап "Build" в Jenkins Pipeline стал завершаться со статусом SUCCESS, и в логах появились строки успешной сборки образа.
