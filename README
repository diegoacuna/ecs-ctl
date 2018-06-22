# ecs-ctl

Manage Amazon ECS like with kubectl.

# Description

ecs-ctl is a small python script useful to perform some common tasks on your ECS clusters. By now you can:

 * List your clusters
 * List your tasks and containers
 * Open a bash session on one of your containers
 
I'm going to add more features later. This software is still on beta so you may face some errors.

# Installation

The easy way (using pip):

```
pip install ecs-ctl
```

If everything goes ok, you should have a *ecs-ctl* command

You also can install the command line utility directly using setuptools:

```
git clone https://github.com/diegoacuna/ecs-ctl.git
cd ecs-ctl
python setup.py install
```

NOTE: this software has been tested on python 2.7 only!

## Using ecs-ctl

To list your clusters on ECS:

```
ecs-ctl list clusters
```

The software will output a list with the full ARN of your clusters.

To list tasks running on your clusters:

```
ecs-ctl list tasks
```

The software will output a table with the information of each tasks per each cluster (if you have more than one cluster you will get more than one table).

If you want to open a bash session on one of your containers, first you need to configure the SSH key to access your
EC2 instances running ECS. You can do this by creating a .ecs_ctl file on your home folder (~/.ecs_ctl) with the next content:

```
[default]
ecsKey=PATH_TO_MY_SSH_KEY
```

The software will automatically detect the key. If you don't want to use this method, you can use the "-k" (--key) parameter when running the software:

```
ecs-ctl exec CONTAINER_NAME bash --key PATH_TO_MY_KEY
```

So, if you want a bash session, you can do:

```
> ecs-ctl list tasks
==========================  Tasks in cluster YOUR_CLUSTER_ARN  ===========================
ARN                          Containers                 Status    Started At
---------------------------- -------------------------  --------  --------------------------------
YOUR_TASK_ARN                CONTAINER_NAME             RUNNING   CONTAINER_STARTED_AT_DATE
```

then:

```
ecs-ctl exec CONTAINER_NAME bash
```

and you will get a prompt on the container specified.

## Help

If you execute the software without any params, you will get the help message:

```
> ecs-ctl
usage: ecs-ctl [-h] [-k KEY] [-d] action [element] [command]

positional arguments:
  action             Action to execute. It can be one of:
                      - get: get information of an element
                      - exec: executes a command in a container
  element            Element where you want to execute the action. It can be one of:
                      - clusters
                      - tasks
  command            Command to execute on the container (for the action exec). For example:
                      - "exec CONTAINER_NAME bash" opens a bash terminal on the CONTAINER_NAME

optional arguments:
  -h, --help         show this help message and exit
  -k KEY, --key KEY  SSH key used to connect to ECS instances
  -d, --debug        Enable debugging of the application

Available Actions:
- get: get elements from ECS. For example: get clusters, get tasks
- exec: executes a command on a container. For example: exec CONTAINER_NAME bash (opens a bash terminal on the container)

 For the exec action you need to provide a SSH key to access the ECS instance running the container. You can do this in two different ways:
 - .ecs_ctl configuration file on your home path (~) with a section [default] and the path of the key in the property ecsKey
 - Using the --key (or -k) parameter of the program
```