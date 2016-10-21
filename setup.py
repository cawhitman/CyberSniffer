from distutils.core import setup

setup(name="honeypot",
      version='0.1',
      description="Detect, capture, and record cyber attacks as they happen",
      packages=[
          'honeypot',
          'honeypot.tests',
      ],
)
