import os
from pathlib import Path

from django.core.management.base import BaseCommand

from apps.styles.models import Style


class Command(BaseCommand):
    help = "Register .pth and .onnx style models from style_models directory"

    def handle(self, *args, **options):
        base_dir = Path(Path(__file__).resolve().parents[4]) / 'style_models'
        if not base_dir.exists():
            self.stdout.write(self.style.WARNING(f"{base_dir} does not exist"))
            return
        for path in base_dir.iterdir():
            if path.suffix not in {'.pth', '.onnx'}:
                continue
            name = path.stem
            framework = path.suffix.lstrip('.')
            style, created = Style.objects.get_or_create(
                name=name,
                defaults={
                    'file_path': str(path),
                    'framework': framework,
                },
            )
            if not created:
                style.file_path = str(path)
                style.framework = framework
                style.save()
                self.stdout.write(f"Updated {name}")
            else:
                self.stdout.write(f"Registered {name}")
