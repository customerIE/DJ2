from django.core.management.base import BaseCommand
from hw2_app.models import Client

class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='UserID') #  pk ��������� ���� ������ id ����� �� �������� ��������� (������� ������ � jango) ��������� �������� �� �������

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        client = Client.objects.filter(pk=pk).first()      # ������ ������ get �� ������� ������ ���� ������ ��������� ��� first() - ������� ������� ���� �� ���������
        self.stdout.write(f'{client}')