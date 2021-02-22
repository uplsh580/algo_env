# Algorithms Env.
This Repo. provides an environment to solving algorithm problems for **BEGINNERS**.
- Python 3.6.10
- GCC 8.3.0

## Install & Start Env.
### Option1. Using Virtual Environment
1. Install virtualenv
    ```
    pip install virtualenv
    ```
3. Clone this repo.
    ```
    git clone https://github.com/uplsh580/algo_env.git
    cd algo_env
    ```
2. Create Virtenv
    ```
    python -m venv .venv
    ``` 
3. Activate virtenv
    ```
    . .venv/bin/activate
    ```
4. Install python packages
    ```
    pip install -r requirement.txt
    ```
### Option2. Using Docker
1. Install **Docker** [link](https://www.docker.com/)
2. Clone this repo.
    ```
    git clone https://github.com/uplsh580/algo_env.git
    cd algo_env
    ```
4. Execute `docker_set.sh` script to build docker image and run container
    ```
    ./docker_setup.sh --run
    ```
2. Check container is created.
    ```
    docker ps -a
    ```
    You can find the `algo` container has UP STATUS.
3. Run bash in `algo` container.
    ```
    docker exec -it algo /bin/bash
    ```
    The executed bash is the shell that ran on the algo container.

#### Don't be embarrassed.
* Q: How to exit from container? <br>
   A: Run `exit` command in container shell.<br>

* Q: When run `docker exec -it algo /bin/bash` command, I meet below message.
    ```
    > docker exec -it algo /bin/bash
    Error response from daemon: Container 3a6c980cfda39555c4ed954c72e7a4bbe166ff1b7acad2386d3fdf5aa4a81e28 is not running
    ```
   A: This is a message that appears after the container is closed. <br>
    Please run `docker start algo` to start container <br>
    and execute again `docker exec -it algo /bin/bash` command.<br>
