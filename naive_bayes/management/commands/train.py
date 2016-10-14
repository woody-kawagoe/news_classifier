from django.core.management.base import BaseCommand
import trainer.getNewslist
import trainer.getNews
import trainer.getClassifier

class Command(BaseCommand):

    def handle(self, *args, **options):
        trainer.getNewslist.getNewslist()
        trainer.getNews.getNews()
        trainer.getClassifier.getClassifier()
