# Generated by Django 2.1.1 on 2018-09-14 01:51

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('append_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commentator',
            fields=[
                ('commentator_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(default='名無しさん', max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='commentator',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='guestbook_plus.Commentator'),
        ),
        migrations.AddField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oyako', to='guestbook_plus.Comment'),
        ),
    ]
