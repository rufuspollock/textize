Online service to take a gutenberg text, strip off the bumpf and make available in different formats such as plain text, html, pdf.

  * Ticket: http://knowledgeforge.net/okfn/tasks/ticket/283
  * Mercurial repo: http://bitbucket.org/rgrp/textize

Copyright 2010 Open Knowledge Foundation. Licensed under AGPL.


= Plan =

== System Structure ==

1. Frontend: catalogue and links to texts in various formats
  * openbiblio
2. Store: with texts (maybe same as frontend)
3. Messaging system
4. Listeners which do cleaning and PDFizing
  * Could plug in other cleaners ...

== Steps ==

=== Frontend ===

1. I come to the Frontend and request Madame Bovary in PDF
2. Frontend looks up in store where PDF exists
  * Yes: return it
  * No: proceed
3. Add PDF task for Madame Bovary to task queue and return to user saying they should check back in 30m

=== Task queue ===

=== Storage server ===

=== Worker ===

1. Worker checks for message for PDFation and finds pdf item
2. Work locates and downloads source text
3. Cleans and up PDFs source text
4. Uploads results to holding/storage server
5. Adds message that this has been done

