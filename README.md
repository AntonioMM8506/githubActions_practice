# GitHub Actions Practice
## PLatzi Object Oriented Programing Course - Platzi

<img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" /> <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white" /> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" /> 

<img src="https://komarev.com/ghpvc/?username=AntonioMM8506"/> [![Python package](https://github.com/AntonioMM8506/githubActions_practice/actions/workflows/ci.yml/badge.svg)](https://github.com/AntonioMM8506/githubActions_practice/actions/workflows/ci.yml)

![Your Repository’s Stats](https://github-readme-stats.vercel.app/api?username=AntonioMM8506&show_icons=true)

### Reprodcution Steps

1. Create an empty repository and commit some files, as a normal project
2. Go to `Actions` tab and select `New Workflow`, for this example I used `Python Package`
3. Edit the yml file in order to fulfill all the requirements you need. For example: how to build the code

If you are gonna use DockerHub

4. Create a Dockerfile in the root of the project
5. Create an entrypoint.sh file in the root of the project
6. Edit the yml file in order to be in the same frequence as the docker files

The yml file in this project is configured so everysingle time a new push or a pull request is triggered in the project, then it will rerun the yml file.

