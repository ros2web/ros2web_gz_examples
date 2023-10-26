from setuptools import setup

package_name = 'simple_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tygoto',
    maintainer_email='tygoto@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'simple_robot = simple_robot.simple_robot:main',
        ],
    },
    package_data={
        'simple_robot': [
            'data/**/*',
        ],
    },
)
