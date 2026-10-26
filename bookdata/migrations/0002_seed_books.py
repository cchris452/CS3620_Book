from django.db import migrations


BOOKS = [
    ("The Glass Orchard", "favorites", "A quiet novel about family, memory, and a garden that changes with the seasons.", 4.6),
    ("Maps for the Moon", "favorites", "A young cartographer sets out to understand the stories behind an old collection of maps.", 4.4),
    ("The Clockwork Grove", "fantasy", "Apprentice inventors discover an enchanted forest hidden beneath their city.", 4.7),
    ("The Ember Crown", "fantasy", "Two rival heirs must work together to protect a kingdom powered by ancient fire.", 4.5),
    ("Signal from Europa", "scifi", "A research crew investigates a repeating transmission beneath the ice of Europa.", 4.6),
    ("The Last Greenhouse", "scifi", "After Earth's climate shifts, a small crew searches space for a place to grow food.", 4.3),
    ("The House at Briar Lake", "horror", "A caretaker hears footsteps in a lakeside house that has stood empty for decades.", 4.2),
    ("Whispers in the Attic", "horror", "A family renovating an old home uncovers a diary that predicts their nights.", 4.4),
    ("A Life in Small Steps", "biography", "The story of a community organizer who built lasting change through local work.", 4.5),
    ("Beyond the Finish Line", "biography", "An athlete reflects on setbacks, training, and the people who shaped a long career.", 4.3),
    ("Letters from the Silk Road", "history", "A collection of connected stories follows merchants traveling across medieval trade routes.", 4.4),
    ("The Harbor Years", "history", "A coastal town records how migration and industry transformed its waterfront.", 4.2),
    ("The Missing Observatory", "mystery", "A determined student investigates the disappearance of a scientist and a star chart.", 4.6),
    ("A Puzzle at Willow House", "mystery", "Guests at a country inn must solve a series of clues before a storm passes.", 4.3),
    ("Build a Better Morning", "selfhelp", "Practical exercises help readers create a thoughtful and sustainable morning routine.", 4.2),
    ("The Art of Listening Well", "selfhelp", "Simple techniques for being more present and communicating with care.", 4.5),
    ("Everyday Astronomy", "education", "An accessible introduction to planets, stars, and observing the night sky.", 4.6),
    ("Numbers in Nature", "education", "Examples from plants, animals, and weather explain patterns in mathematics.", 4.4),
    ("Rain on the Windowsill", "poetry", "A collection of short poems about home, changing weather, and ordinary moments.", 4.5),
    ("Field Notes at Dusk", "poetry", "Poems trace a year of walks through woodland and open fields.", 4.3),
]


def seed_books(apps, schema_editor):
    BookData = apps.get_model("bookdata", "BookData")
    for name, category, description, rating in BOOKS:
        BookData.objects.get_or_create(
            name=name,
            category=category,
            defaults={"description": description, "rating": rating},
        )


class Migration(migrations.Migration):

    dependencies = [
        ("bookdata", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_books, migrations.RunPython.noop),
    ]