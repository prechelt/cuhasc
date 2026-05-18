from django.db import models

import cuhasc.base as base
import cuhasc.constants as c


class Team(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=c.TOKEN_LENGTH_TEAM)

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = base.random_token(c.TOKEN_LENGTH_TEAM)
        super().save(*args, **kwargs)
