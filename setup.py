from setuptools import setup

setup(
    name="ecs-ctl",
    version="0.1.2",
    author="Diego A.",
    author_email="diego.acuna@mailbox.org",
    url="https://github.com/diegoacuna/ecs-ctl",
    description="Manage Amazon ECS like with kubectl",
    long_description="Manage Amazon ECS like with kubectl. ecs-ctl is a small python script useful to perform some common tasks on your ECS clusters. By now you can:\n * List your clusters\n * List your tasks and containers\n * Open a bash session on one of your containers\n. For more information, visit the homepage of the package.",
    license='MIT',
    # Dependent packages (distributions)
    install_requires=[
        "boto3",
        "tabulate"
    ],
    scripts=['bin/ecs-ctl']
)
