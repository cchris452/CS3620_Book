from django.db import migrations


BOOKS = [
    ("The Blue Hour Kitchen", "favorites", "A neighborhood cook brings people together through recipes passed between generations.", 4.5),
    ("Small Wonders of Home", "favorites", "Short reflections celebrate the overlooked details that make a place feel like home.", 4.2),
    ("The Lantern Cartographer", "favorites", "An illustrator inherits a collection of maps that leads her back to her hometown.", 4.6),
    ("The Fox and the Fallen Star", "fantasy", "A young fox follows a fallen star into a kingdom hidden beneath the hills.", 4.4),
    ("The Orchard of Spells", "fantasy", "Siblings discover that the fruit in their grandmother's orchard grants unusual abilities.", 4.7),
    ("The River's Secret Name", "fantasy", "A ferryman's apprentice must restore the forgotten names of a magical river.", 4.3),
    ("Orbit of Quiet Suns", "scifi", "A maintenance crew aboard a remote station finds evidence of a vanished expedition.", 4.5),
    ("The Archive of Tomorrow", "scifi", "A librarian discovers messages from possible futures stored in an abandoned database.", 4.6),
    ("Tides Beyond Saturn", "scifi", "Scientists on an ocean moon investigate a signal rising from beneath the waves.", 4.4),
    ("The Hollow at Marrow Hill", "horror", "A hiking group takes shelter near a village that appears on no current map.", 4.3),
    ("Night Shift at the Museum", "horror", "A new guard notices that one gallery changes whenever the lights go out.", 4.5),
    ("The House That Kept the Rain", "horror", "A family moves into a house where storms gather even under clear skies.", 4.2),
    ("A Voice for the Valley", "biography", "The life of a teacher who helped rural students gain access to higher education.", 4.4),
    ("On the Open Water", "biography", "A marine biologist recounts decades of discovery, conservation, and life at sea.", 4.6),
    ("The Long Way to the Stage", "biography", "A performer looks back on the mentors and turning points behind a creative career.", 4.3),
    ("The City Beneath the Sand", "history", "Archaeological discoveries reveal how an ancient desert settlement managed water.", 4.5),
    ("A Winter at the Telegraph", "history", "Letters and records tell the story of a frontier town connected by a new telegraph line.", 4.2),
    ("The Makers of the Printing Press", "history", "The people and workshops behind the spread of early printed books come to life.", 4.4),
    ("The Case of the Painted Key", "mystery", "A museum conservator investigates a theft linked to a series of unusual paintings.", 4.5),
    ("Footprints at Cedar Point", "mystery", "A park ranger follows a trail of clues after a visitor disappears before sunrise.", 4.3),
    ("The Baker's Last Recipe", "mystery", "A food writer deciphers a baker's notes to uncover the truth behind an old dispute.", 4.6),
    ("Make Room for Rest", "selfhelp", "A practical guide to setting boundaries and building more restorative routines.", 4.4),
    ("The Patient Practice", "selfhelp", "Small, repeatable exercises help readers approach long-term goals with patience.", 4.3),
    ("Conversations That Connect", "selfhelp", "Readers learn ways to ask better questions and navigate difficult discussions.", 4.5),
    ("Weather for Curious Minds", "education", "Clear experiments and illustrations explain clouds, storms, and changing climates.", 4.6),
    ("The Living Map", "education", "An introduction to ecosystems shows how plants, animals, and habitats depend on one another.", 4.4),
    ("How Bridges Stand", "education", "Everyday examples introduce the forces and designs that keep bridges stable.", 4.5),
    ("A Map of Falling Leaves", "poetry", "Seasonal poems follow a walking path from the first warm days to late autumn.", 4.4),
    ("The Shape of Blue", "poetry", "Brief poems explore the many shades of water, distance, and longing.", 4.6),
    ("Songs for the Early Train", "poetry", "A collection of city poems captures quiet moments before the morning rush.", 4.3),
    ("The Lantern and the Tide", "favorites", "A seaside shopkeeper restores lost heirlooms and discovers a story hidden in their tide marks.", 4.5),
    ("Paper Stars on Maple Street", "favorites", "A young illustrator learns how every block in her neighborhood holds a different kind of homecoming.", 4.4),
    ("Wren of the Broken Bell", "fantasy", "A bellringer with a missing memory must wake an ancient city before the bell falls silent forever.", 4.6),
    ("The Dragon in the Salt Marsh", "fantasy", "A stubborn mapmaker and a dragon guard the last safe passage through a stormy estuary.", 4.3),
    ("Dawn Below the Solar Sea", "scifi", "An undersea colony tracks a strange glow that appears every sunrise along the ocean floor.", 4.6),
    ("The Last Colony on Vesper", "scifi", "A crew of settlers learns that their new home has been waiting for a message no one was meant to send.", 4.4),
    ("The Red Room at St. Hale", "horror", "A reporter investigates a closed room in an old hospital that only appears at midnight.", 4.5),
    ("Winter Under the Chapel Floor", "horror", "A church renovation reveals a hidden chamber filled with names and unfinished prayers.", 4.2),
    ("The Quiet Promise of Ash", "biography", "A firefighter reflects on the communities that carried him through his most difficult years.", 4.5),
    ("Ribbons for the River", "biography", "An activist chronicles village campaigns, river cleanups, and the patience required for change.", 4.4),
    ("A City of Glass and Iron", "history", "A memoir of industry and migration traces the growth of a city built on steel and smoke.", 4.3),
    ("The Last Ship to Brineport", "history", "A harbor town remembers the crews and families who kept trade alive through hard seasons.", 4.4),
    ("The Girl Who Counted Comets", "mystery", "A math prodigy uncovers a pattern in a series of disappearances across the observatory district.", 4.6),
    ("The Locked Archive of Bellwood", "mystery", "When a library vault refuses to open, a historian follows the trail of one missing ledger.", 4.3),
    ("Thirteen Minutes to Morning", "selfhelp", "Simple routines and reflection prompts help readers turn stress into steadier habits.", 4.4),
    ("The Gentle Habit", "selfhelp", "A practical look at small rituals that create calm, focus, and lasting resilience.", 4.5),
    ("Beyond the Classroom Wall", "education", "Case studies from museums, farms, and labs show how learning continues outside school.", 4.4),
    ("The Hidden Geometry of Birds", "education", "A vivid field guide explores the shapes, paths, and patterns that make flight possible.", 4.6),
    ("Moonlit Margins", "poetry", "Short lyrics capture waiting rooms, midnight buses, and the quiet hopes of city life.", 4.5),
    ("Larkspur in the Alley", "poetry", "Poems about gardens, grief, and second chances bloom in a city courtyard.", 4.3),
    ("The Orchard of Echoes", "favorites", "A family orchard hides a chorus of memories that return when the fruit ripens each autumn.", 4.5),
    ("A Thread of Summer Gold", "favorites", "An old sewing room becomes the place where a young artist learns to trust her own voice.", 4.4),
    ("The Cinder Court", "fantasy", "A fallen princess must navigate a court of ash, grudges, and stolen prophecies.", 4.6),
    ("The Bone Map of Kestrel", "fantasy", "A treasure hunter follows a map drawn in bone and moonlight to a forgotten kingdom.", 4.2),
    ("Ash on the Rings of Mars", "scifi", "A rover engineer uncovers evidence that a long-lost mission never really ended.", 4.5),
    ("The Titanium Meadow", "scifi", "On a frontier moon, a botanist discovers a field of metal flowers growing beneath the ice.", 4.4),
    ("The Door Under the Stairs", "horror", "A child discovers a hidden door in her home that opens onto a house that remembers her.", 4.3),
    ("Whispering Hallway Nine", "horror", "A university dormitory develops a reputation for doors that open to rooms no one has entered.", 4.5),
    ("My Name Became a River", "biography", "A memoir follows one artist's search for belonging through migration, craft, and memory.", 4.6),
    ("The Weight of the Tide", "biography", "A sailor recounts years of work, weather, and the lessons carried by a long coastline.", 4.4),
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
        ("bookdata", "0002_seed_books"),
    ]

    operations = [
        migrations.RunPython(seed_books, migrations.RunPython.noop),
    ]
