This application can be run in either Docker or as a standalone python application

## I. Run inside Docker
  1. Install [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
  2. Goto directory where there is dockerfile  
  3. To build the docker image execute command:
          ```bash
          docker build . -t <web_app_name>
          ```
  4. To run the docker container execute command:
          ```bash
            docker run -p 8080:8080 <web_app_name>
          ```        
  Access the following urls in the browser:
  
    1. http://0.0.0.0:8080/ping

    2. http://0.0.0.0:8080/system
 
    3. http://0.0.0.0:8080/mediainfo/11497188 or other images present in pond5 website

## II. Run standalone 
  1. Install [python](https://www.python.org/downloads/)
  2.  ```bash
        cd  pond_web_service
      ```  
  3.  ```bash
        pip install -r requirements.txt
       ```
  4.  ```bash
       python app.py
      ```

