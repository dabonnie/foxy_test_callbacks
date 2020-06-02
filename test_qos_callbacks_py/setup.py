from setuptools import setup

package_name = 'test_qos_callbacks_py'

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
    maintainer='dbbonnie',
    maintainer_email='dbbonnie@amazon.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker_incompatible = test_qos_callbacks_py.talker_incompatible:main',
            'listener_default = test_qos_callbacks_py.listener_default:main',
            'listener_custom = test_qos_callbacks_py.listener_custom:main',
        ],
    },
)
