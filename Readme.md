This application can be run in either Docker or as a standalone python application
Steps to run it in docker
  
  1. Goto directory where there is dockerfile  
  2. To build the docker image execute command:
          docker build . -t <web_app_name>
  3. To run the docker container execute command:
          docker run -p 8080:8080 <web_app_name>
          
  Access the following urls in the browser:
  
    1. http://0.0.0.0:8080/ping

    2. http://0.0.0.0:8080/system
 
    3. http://0.0.0.0:8080/mediainfo/11497188 or other images present in pond5 website



