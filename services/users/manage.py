import unittest
import coverage

from flask.cli import FlaskGroup
from project import create_app, db
from project.api.models import User
from pathlib import Path


coverage_path = Path(__file__).parent.joinpath('.coverage').resolve()
coverage_config = Path(__file__).parent.joinpath('.coveragerc').resolve()
print(f'path to .coverage: {coverage_path}.')
COV = coverage.coverage(
    data_file=str(coverage_path),
    config_file=str(coverage_config)
)
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@cli.command()
def seed_db():
    """seeds the database"""
    db.session.add(User(username='nd', email='nd@mherman.org'))
    db.session.add(User(username='nc', email='nc@mherman.org'))
    db.session.commit()


@cli.command()
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('project/tests')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    return 1


if __name__ == '__main__':
    cli()
