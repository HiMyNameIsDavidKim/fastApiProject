create table users(
    id primary key = models.AutoField(primary_key=True),
    username varchar(100) = models.CharField(max_length=100),
    pwd varchar(255) = models.CharField(max_length=255),
    created_at date = models.DateField(auto_now=True),
    ranks integer = models.IntegerField(default=1),
    points integer = models.IntegerField(default=0),
)