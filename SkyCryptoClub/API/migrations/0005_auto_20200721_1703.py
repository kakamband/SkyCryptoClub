# Generated by Django 3.0.8 on 2020-07-21 17:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_ipban'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(default='Message')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('valid_until', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Announcement',
                'verbose_name_plural': 'Announcements',
            },
        ),
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Account', 'verbose_name_plural': 'Accounts'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'verbose_name': 'Currency', 'verbose_name_plural': 'Currencies'},
        ),
        migrations.AlterModelOptions(
            name='exchange',
            options={'verbose_name': 'Exchange', 'verbose_name_plural': 'Exchanges'},
        ),
        migrations.AlterModelOptions(
            name='exchangestatus',
            options={'verbose_name': 'Exchange Status', 'verbose_name_plural': 'Exchange Statuses'},
        ),
        migrations.AlterModelOptions(
            name='exchangetaxpeer',
            options={'verbose_name': 'Exchange Tax Peer', 'verbose_name_plural': 'Exchange Taxes Peer'},
        ),
        migrations.AlterModelOptions(
            name='faqcategory',
            options={'verbose_name': 'FAQ Category', 'verbose_name_plural': 'FAQ Categories'},
        ),
        migrations.AlterModelOptions(
            name='founddeposit',
            options={'verbose_name': 'Found Deposit', 'verbose_name_plural': 'Found Deposits'},
        ),
        migrations.AlterModelOptions(
            name='invitation',
            options={'verbose_name': 'Invitation', 'verbose_name_plural': 'Invitations'},
        ),
        migrations.AlterModelOptions(
            name='ipban',
            options={'verbose_name': 'IP Ban', 'verbose_name_plural': 'IP Bans'},
        ),
        migrations.AlterModelOptions(
            name='languages',
            options={'verbose_name': 'Language', 'verbose_name_plural': 'Languages'},
        ),
        migrations.AlterModelOptions(
            name='passwordtoken',
            options={'verbose_name': 'Password Token', 'verbose_name_plural': 'Password Tokens'},
        ),
        migrations.AlterModelOptions(
            name='platform',
            options={'verbose_name': 'Platform', 'verbose_name_plural': 'Platforms'},
        ),
        migrations.AlterModelOptions(
            name='platformcurrency',
            options={'verbose_name': 'Platform Currency', 'verbose_name_plural': 'Platform Currencies'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterModelOptions(
            name='profileban',
            options={'verbose_name': 'Profile Ban', 'verbose_name_plural': 'Profile Bans'},
        ),
        migrations.AlterModelOptions(
            name='publicitybanners',
            options={'verbose_name': 'Publicity Banner', 'verbose_name_plural': 'Publicity Banners'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='supportcategory',
            options={'verbose_name': 'Support Category', 'verbose_name_plural': 'Support Categories'},
        ),
        migrations.AlterModelOptions(
            name='supportticket',
            options={'verbose_name': 'Support Ticket', 'verbose_name_plural': 'Support Tickets'},
        ),
        migrations.AlterModelOptions(
            name='supportticketmessage',
            options={'verbose_name': 'Support Ticket Message', 'verbose_name_plural': 'Support Ticket Messages'},
        ),
        migrations.AlterModelOptions(
            name='twofactorlogin',
            options={'verbose_name': '2FA Code', 'verbose_name_plural': '2FA Codes'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'User Role', 'verbose_name_plural': 'User Roles'},
        ),
        migrations.AlterModelOptions(
            name='wallet',
            options={'verbose_name': 'Wallet', 'verbose_name_plural': 'Wallets'},
        ),
        migrations.AlterModelOptions(
            name='withdrawal',
            options={'verbose_name': 'Withdrawal', 'verbose_name_plural': 'Withdrawals'},
        ),
        migrations.CreateModel(
            name='ReadAnnouncement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Announcement')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Profile')),
            ],
            options={
                'verbose_name': 'Read Announcement',
                'verbose_name_plural': 'Marked as Read Announcements',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('message', models.TextField(default='Message')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.Profile')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
    ]
