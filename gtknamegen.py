#!/usr/bin/python3
"""GTK front-end to the pattern based name generator"""

# SPDX-FileCopyrightText: 2021 Jeff Epler
#
# SPDX-License-Identifier: GPL-3.0-only

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk  # pylint: disable=wrong-import-position

from namegen import namegen  # pylint: disable=wrong-import-position


def on_activate(app):  # pylint: disable=too-many-locals
    """Build the main application"""
    try:
        win = Gtk.ApplicationWindow(application=app)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        win.add(box)

        box.pack_start(Gtk.Label(label="Template:"), False, True, 0)

        pattern_store = Gtk.ListStore(str, str)
        patterns = [
            ("Simple names", "!ss<s|>"),
            ("Apostrophic Names", "!c'Cvs"),
            ("Insults", "!ii"),
            ("Pet Names", "!mM"),
            ("Cute Insults", "!iM"),
            (
                "Greek Names",
                "!<s<v|V>(tia)|s<v|V>(os)|B<v|V>c(ios)|B<v|V><c|C>v(ios|os)>",
            ),
            ("Latin placenames", "!sv(nia|lia|cia|sia)"),
            ("Dragons (Pern)", "!<<s|ss>|<VC|vC|B|BVs|Vs>><v|V|v|<v(l|n|r)|vc>>(th)"),
            ("Dragon Riders", "!c'<s|cvc>"),
            ("Pokemon", "!<i|s>v(mon|chu|zard|rtle)"),
            (
                "Fantasy (R)",
                "!(|(<B>|s|h|ty|ph|r))(i|ae|ya|ae|eu|ia|i|eo|ai|a)(lo|la|sri|da|dai|the|sty|lae|due|li|lly|ri|na|ral|sur|rith)(|(su|nu|sti|llo|ria|))(|(n|ra|p|m|lis|cal|deu|dil|suir|phos|ru|dru|rin|raap|rgue))",
            ),
            (
                "Fantasy (S, A)",
                "!(cham|chan|jisk|lis|frich|isk|lass|mind|sond|sund|ass|chad|lirt|und|mar|lis|il|<BVC>)(jask|ast|ista|adar|irra|im|ossa|assa|osia|ilsa|<vCv>)(|(an|ya|la|sta|sda|sya|st|nya))",
            ),
            (
                "Fantasy (H, L)",
                "!(ch|ch't|sh|cal|val|ell|har|shar|shal|rel|laen|ral|jh't|alr|ch|ch't|av)(|(is|al|ow|ish|ul|el|ar|iel))(aren|aeish|aith|even|adur|ulash|alith|atar|aia|erin|aera|ael|ira|iel|ahur|ishul)",
            ),
            (
                "Fantasy (N, L)",
                "!(ethr|qil|mal|er|eal|far|fil|fir|ing|ind|il|lam|quel|quar|quan|qar|pal|mal|yar|um|ard|enn|ey)(|(<vc>|on|us|un|ar|as|en|ir|ur|at|ol|al|an))(uard|wen|arn|on|il|ie|on|iel|rion|rian|an|ista|rion|rian|cil|mol|yon)",
            ),
            (
                "Fantasy (K, N)",
                "!(taith|kach|chak|kank|kjar|rak|kan|kaj|tach|rskal|kjol|jok|jor|jad|kot|kon|knir|kror|kol|tul|rhaok|rhak|krol|jan|kag|ryr)(<vc>|in|or|an|ar|och|un|mar|yk|ja|arn|ir|ros|ror)(|(mund|ard|arn|karr|chim|kos|rir|arl|kni|var|an|in|ir|a|i|as))",
            ),
            (
                "Fantasy (J, G, Z)",
                "(aj|ch|etz|etzl|tz|kal|gahn|kab|aj|izl|ts|jaj|lan|kach|chaj|qaq|jol|ix|az|biq|nam)(|(<vc>|aw|al|yes|il|ay|en|tom||oj|im|ol|aj|an|as))(aj|am|al|aqa|ende|elja|ich|ak|ix|in|ak|al|il|ek|ij|os|al|im)",
            ),
            (
                "Fantasy (K, J, Y)",
                "!(yi|shu|a|be|na|chi|cha|cho|ksa|yi|shu)(th|dd|jj|sh|rr|mk|n|rk|y|jj|th)(us|ash|eni|akra|nai|ral|ect|are|el|urru|aja|al|uz|ict|arja|ichi|ural|iru|aki|esh)",
            ),
            (
                "Fantasy (S, E)",
                "(syth|sith|srr|sen|yth|ssen|then|fen|ssth|kel|syn|est|bess|inth|nen|tin|cor|sv|iss|ith|sen|slar|ssil|sthen|svis|s|ss|s|ss)(|(tys|eus|yn|of|es|en|ath|elth|al|ell|ka|ith|yrrl|is|isl|yr|ast|iy))(us|yn|en|ens|ra|rg|le|en|ith|ast|zon|in|yn|ys)",
            ),
        ]
        for p in patterns:
            pattern_store.append(p)

        entry = Gtk.ComboBox.new_with_model_and_entry(pattern_store)
        entry.get_child().set_text(pattern_store[0][1])
        entry.set_entry_text_column(0)
        box.pack_start(entry, False, True, 0)

        store = Gtk.ListStore(str)
        tree = Gtk.TreeView(model=store)

        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Generated", renderer, text=0)
        tree.append_column(column)
        tree.set_activate_on_single_click(True)

        clipboard = Gtk.Clipboard.get_default(win.get_display())

        def copy_row_text(listbox, path, column):  # pylint: disable=unused-argument
            text = store[path][0]
            clipboard.set_text(text, len(text))

        tree.connect("row_activated", copy_row_text)

        def gen():
            template = entry.get_child().get_text()
            for i in patterns:
                if i[0] == template:
                    template = i[1]
                    entry.get_child().set_text(template)
            try:
                names = [[namegen(template)] for i in range(10)]
            except Exception as e:  # pylint: disable=broad-except
                names = [[str(e)]]
            store.clear()
            for i in names:
                store.append(i)

        gen()
        box.pack_start(tree, True, True, 0)

        button = Gtk.Button(label="Regenerate")
        box.pack_start(button, False, True, 0)
        button.connect("clicked", lambda _: gen())

        entry.connect("changed", lambda _: gen())
        win.show_all()
        win.present()

    except Exception:  # pylint: disable=broad-except
        app.quit()
        raise


app_ = Gtk.Application(application_id="net.unpy.namegen")
app_.connect("activate", on_activate)
app_.run(None)
