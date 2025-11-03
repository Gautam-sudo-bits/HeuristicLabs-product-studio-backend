# prompt_templates
SOLID_BACKGROUND_INSTRUCTION = """
===== STUDIO BACKGROUND IMAGE GENERATION - STRICT PROTOCOL =====
YOU MUST FOLLOW THESE STEPS IN EXACT ORDER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: ANALYZE INPUT IMAGE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IF INPUT IMAGE IS PROVIDED:
Examine the image carefully and extract these EXACT details:
A) PRODUCT IDENTITY:
What is the exact product shown?
Specific model characteristics, design features
B) PHYSICAL ATTRIBUTES:
Precise colors (include hex codes if discernible):
Material finishes (matte/glossy/textured/metallic, etc.,):
Shape and form factor:
Dimensions and proportions:
C) BRAND ELEMENTS (CRITICAL - PRESERVE EXACTLY):
Any visible logos (describe position, style, clarity):
Any text/labels on product (transcribe exactly as shown, even if blurry):
Any badges, stickers, brand marks:
Typography style if readable:
D) COMPONENT DETAILS:
Buttons, knobs, controls, screens:
Handles, legs, stands, attachments:
Openings, vents, ports, connectors:
Surface textures and patterns:
Stitching, seams, joints (for fabric/leather products):
E) CURRENT STATE:
Product condition in image:
Any wear, reflections, or characteristics to maintain:
WRITE THIS ANALYSIS EXPLICITLY BEFORE GENERATING THE PROMPT.
IF NO INPUT IMAGE:
Use the provided product type to describe a standard, accurate representation of that product category.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: CONSTRUCT STUDIO SCENE SPECIFICATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Now define the studio setup:

BACKGROUND:

Color: [Choose ONE: Pure white (#FFFFFF) / Light gray (#F5F5F5) / Soft beige (#FAF9F6) / Pale neutral tone]

Texture: Seamless, perfectly smooth, gradient-free

Type: Infinity curve backdrop OR flat surface with reflective floor

PRODUCT POSITIONING:

Placement: Centered in frame

Angle: [Select based on product type]

Small items (jewelry, accessories, phones): Slightly elevated, 30-45° angle

Appliances/Electronics: Front-facing 3/4 view showing controls and main features

Furniture: Front or angled view showing design and legs

Fashion/Apparel: Flat lay OR hanging OR on invisible mannequin

Tools/Equipment: Angled to show primary functional side

Distance: 15-20% margin from all frame edges

LIGHTING SETUP:

Primary: Three-point studio lighting (key + fill + rim)

Quality: Soft, diffused, professional

Shadows: Subtle, falling to [left/right/back] opposite key light, 30-40% opacity

Reflections: Natural floor reflection showing 40-50% opacity of product base

Highlights: Gentle specular highlights on shiny surfaces without overexposure

PRODUCT STATE:

Condition: Pristine, brand new appearance

Operational status: OFF/CLOSED/RESTING (no power, no operation)

Configuration: [Specify based on product - doors closed, screens off, blades retracted, etc.]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: GENERATE FINAL PROMPT WITH STRICT FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OUTPUT FORMAT (USE EXACTLY THIS STRUCTURE):

"Professional studio product photography.

PRODUCT: [Insert EXACT description from Step 1 - all physical details, colors, materials, dimensions]. [CRITICAL: List ALL brand text/logos exactly as they appear, with exact positioning]. [List all components, buttons, features from Step 1].

SCENE: Product isolated and centered on [background color] seamless infinity backdrop. Product positioned at [specific angle from Step 2].

LIGHTING: Professional three-point studio lighting with soft diffused key light from [direction], fill light reducing shadows, rim light creating edge definition. Soft shadow cast [direction] at 30-40% opacity. Natural reflection beneath product on glossy floor at 40-50% opacity showing product underside.

STATE: Product in pristine, non-operational condition, [specific state - powered off/closed/resting].

TECHNICAL: High-resolution commercial product photography, tack-sharp focus throughout entire product, no depth-of-field blur, neutral white balance (5500K), minimal lens distortion, e-commerce platform ready.

PRESERVE: Exact product appearance from input image including all logos, text, material finishes, and design details without any alterations."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY CHECKS BEFORE SUBMITTING PROMPT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Have I described the EXACT product from the input image with specific details?
□ Have I listed ALL visible brand text/logos exactly as shown?
□ Have I specified exact colors, materials, and finishes from the input?
□ Is the background a solid studio color (not lifestyle scene)?
□ Is the product state non-operational?
□ Have I included studio lighting with shadows and reflections?
□ Is the output format followed precisely?

CRITICAL REMINDER: You are NOT creating a new product. You are describing how to photograph the EXACT product shown in the input image in a professional studio setting. Every detail must match the input.

***Generate the detailed product description from Step 1 and final prompt (Step 3) for the product imgage provided.*** 
"""

LIFESTYLE_INSTRUCTION = """
===== LIFESTYLE IMAGE GENERATION - STRICT PROTOCOL =====

YOU MUST FOLLOW THESE STEPS IN EXACT ORDER:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: ANALYZE INPUT IMAGE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IF INPUT IMAGE IS PROVIDED:
Examine the image and document these EXACT details:

A) PRODUCT COMPLETE DESCRIPTION:

Exact product type and model:

Precise color palette (all colors present):

Material composition (fabric/metal/plastic/wood/glass/leather):

Texture and finish (matte/glossy/brushed/woven/smooth):

Exact dimensions and proportions:

B) BRAND PRESERVATION (MUST MAINTAIN):

All visible logos (position, size, clarity level):

All text on product (exact wording, even if partially visible or blurry):

Brand marks, symbols, badges:

Maintain the same viewing angle/ camera angle as in the input product image if possible.

Color schemes associated with branding:

C) DESIGN FEATURES:

All buttons, controls, displays, interfaces:

Structural elements (handles, wheels, stands, feet, lids):

Unique design characteristics:

Any attachments or accessories visible:

WRITE THIS ANALYSIS EXPLICITLY.

IF NO INPUT IMAGE:
Describe standard accurate features of the stated product type.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: DETERMINE SCENE TYPE FROM THEME GUIDELINES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Read the Theme Guidelines and decide:

OPTION A - WITH HUMAN INTERACTION:
(If guidelines mention: person, man, woman, model, someone using, human interaction, etc.)

Define human subject:

Type: [man/woman/young adult/child/professional/athlete - based on product and theme]

Approximate age: [age range appropriate to product]

Ethnicity/appearance: [diverse, natural, relatable - based on theme]

Clothing: [Specific attire matching environment and activity]

Expression: [Specific: warm smile/focused/relaxed/confident/joyful]

Pose detail: [SPECIFIC pose - e.g., "standing with left hand resting on product, right hand in pocket, left leg slightly forward, looking at camera with gentle smile"]

Eye direction: [looking at camera OR looking at product OR looking away naturally]

OPTION B - STANDALONE PRODUCT:
(If guidelines mention: product alone, no people, standalone, product focus, etc.)

Define contextual props:

Supporting items that suggest product use

Environmental elements that tell product story

Props positioned to complement, not compete, aim for real-world natural setting depiction.

STATE YOUR CHOICE: [ ] Option A - Human Interaction  [ ] Option B - Standalone

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: DEFINE LOGICAL ENVIRONMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Based on product type, select appropriate setting where this product ACTUALLY exists/is used:

ENVIRONMENT LOGIC TABLE:

Coffee makers/Kitchen appliances → Kitchen counter, breakfast nook, home kitchen

Outdoor power equipment → Driveway, yard, garage, appropriate outdoor terrain

Fitness equipment → Home gym, yoga studio, fitness room, outdoor exercise space

Electronics/Gaming → Living room, home office, entertainment area, desk setup

Fashion/Accessories → Urban café, home bedroom, outdoor lifestyle location

Beauty products → Bathroom vanity, spa-like setting, bedroom dresser

Tools → Workshop, garage workbench, construction site (if commercial)

Furniture → Living room, bedroom, patio, appropriately decorated space

Baby/Kids products → Nursery, playroom, family living area

Automotive accessories → Garage, driveway, car interior

SELECTED ENVIRONMENT: [Specific setting based on above logic]

ENVIRONMENTAL DETAILS:

Primary surface: [What product sits on/near]

Background elements: [3-5 specific items visible in background]

Environmental storytelling: [Evidence of product's purpose WITHOUT showing it working]
Examples:

Snow blower → Cleared path behind, deep snow in front

Coffee maker → Filled cup beside machine, coffee beans nearby

Vacuum → Clean, tidy room environment

Lawn mower → Freshly cut grass edge, outdoor setting

Depth: [Sharp throughout OR soft background blur keeping product sharp]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4: DEFINE LIGHTING & ATMOSPHERE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

LIGHTING TYPE:
[ ] Natural window light (soft, directional)
[ ] Golden hour sunlight (warm, low-angle)
[ ] Bright daylight (even, clear)
[ ] Soft overcast (diffused, no harsh shadows)
[ ] Warm interior lighting (cozy, ambient)

SELECTED: [Choose based on theme and environment]

ATMOSPHERIC MOOD:

Color temperature: [Warm/Neutral/Cool]

Overall feeling: [Cozy/Fresh/Energetic/Serene/Professional]

Shadow quality: Soft and natural

Time of day suggestion: [Morning/Midday/Afternoon/Evening]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5: GENERATE FINAL PROMPT WITH STRICT FORMAT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FOR HUMAN INTERACTION (Option A):

"Lifestyle product photography with human interaction.

PRODUCT: [EXACT description from Step 1 - all colors, materials, finishes, dimensions, visible text/logos with exact wording and positioning, all design features and components]. Product in non-operational, resting state.

HUMAN SUBJECT: [Detailed description from Step 2 - specific age, gender, ethnicity, exact clothing description], [exact detailed pose with body positioning], [facial expression], [eye direction].

PRODUCT INTERACTION: [Specific description of how human is positioned relative to product - e.g., "standing beside product with right hand resting on top surface, casual lean" OR "holding product naturally in both hands at chest height"].

ENVIRONMENT: [Specific setting from Step 3], [surface product is on], [3-5 specific background elements], [environmental storytelling details showing product purpose evidence].

COMPOSITION: Product remains clearly visible occupying 30-40% of frame, human subject complementing but not overshadowing product, [rule of thirds/balanced composition].

LIGHTING: [Specific lighting type from Step 4], [color temperature], creating [atmospheric mood], soft natural shadows, realistic and inviting ambiance.

TECHNICAL: Photorealistic lifestyle photography, natural perspective, [depth of field specification], authentic moment, e-commerce ready.

PRESERVE: Exact product appearance from input image with all logos, text, and design details maintained without alteration."

FOR STANDALONE (Option B):

"Lifestyle product photography, standalone presentation.

PRODUCT: [EXACT description from Step 1 - all colors, materials, finishes, dimensions, visible text/logos with exact wording and positioning, all design features and components]. Product in non-operational, resting state.

PRODUCT POSITIONING: [Specific placement and angle in environment].

CONTEXTUAL PROPS: [Specific complementary items from Step 2 - e.g., "White ceramic mug positioned beneath espresso spout, scattered whole coffee beans on counter surface, small milk pitcher to the right"].

ENVIRONMENT: [Specific setting from Step 3], [surface details], [background elements creating context], [environmental storytelling showing product purpose without operation].

COMPOSITION: Product as hero element in foreground, [specific framing], contextual environment supporting product story.

LIGHTING: [Specific lighting type from Step 4], [color temperature], creating [atmospheric mood], soft natural shadows, authentic setting.

TECHNICAL: Photorealistic lifestyle photography, natural perspective, [depth of field specification], authentic context, e-commerce ready.

PRESERVE: Exact product appearance from input image with all logos, text, and design details maintained without alteration."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANDATORY CHECKS BEFORE SUBMITTING:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Have I described the EXACT product from input with all specific details?
□ Have I preserved ALL brand text/logos exactly as shown?
□ Is the environment logical for where this product is actually used?
□ Is the product in NON-OPERATIONAL state?
□ If human included, is the pose specifically detailed?
□ Are contextual props appropriate and specific?
□ Does environmental storytelling show product purpose without showing it working?

CRITICAL: You are describing how to photograph the EXACT input product in a realistic lifestyle context, not inventing a new product.

NOTE:
***Generate the detailed product description from Step 1 and final prompt (Step 3) for the product imgage provided.*** 
"""

MARKETING_CREATIVE_INSTRUCTION = """
===== MARKETING CREATIVE IMAGE GENERATION - STRICT PROTOCOL =====
YOU MUST FOLLOW THESE STEPS IN EXACT ORDER:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 1: ANALYZE INPUT IMAGE (MANDATORY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

IF INPUT IMAGE IS PROVIDED:
Document EXACT product specifications:
COMPLETE PRODUCT DESCRIPTION:
Product type and specific model:
All colors (precise shades):
All materials and finishes:
Exact proportions and size:
ALL visible brand text/logos (exact wording, position, clarity):
All design features (buttons, screens, handles, components):
Unique identifying characteristics:
WRITE EXPLICIT ANALYSIS.
IF NO INPUT IMAGE: Use accurate standard features of stated product type.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 2: EXTRACT MARKETING SPECIFICATIONS FROM USER INPUT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
From "Marketing Image Details" provided by user, extract:
[NEW] CREATIVE VIBE / TARGET AUDIENCE: (This is the most critical new choice)
Select a vibe based on the product category or user request. This choice will dictate the options in subsequent steps.
[ ] A - MINIMAL & PROFESSIONAL: For hardware, home decor, kitchenware, corporate products, B2B. Focus is on clarity, elegance, and a premium feel.
[ ] B - ENERGETIC & TRENDY (GEN Z FOCUS): For electronics, fashion, jewelry, food, cosmetics, entertainment. Focus is on excitement, high energy, and modern social media trends.
SELECTED VIBE: [Choose one: A or B]
TEXT ELEMENTS:
Brand Name: "[exact text]" OR [none provided]
Headline Text: "[exact text, max 3-4 words]" OR [none provided]
Call-to-Action: "[exact text]" OR default to "SHOP NOW"
Footer Text: "[exact text]" OR [none]
PROMOTIONAL ELEMENTS:
Discount/Sale callout: "[e.g., 50% OFF, LIMITED TIME, NEW]" OR [none]
Badge/Banner needed: [YES/NO] - "[text if yes]"
SEASONAL/FESTIVE THEME:
Theme: [Christmas/New Year/Black Friday/Summer/Spring/Halloween/Valentine's/None]
Specific elements required: [e.g., "string lights, snowflakes, ornaments"] related to the festive theme.
[UPDATED] COMPOSITION STYLE:

A - Hero Product (single large product, 60-70% of frame)

B - Multi-Instance (2-5 products at varying sizes/angles)

C - Feature Showcase (main product + detail callouts)

D - Lifestyle + Overlay (lifestyle scene with promotional graphics)
[NEW] [ ] E - Dynamic Asymmetry (Product is off-center, balanced by bold text and graphic elements)
[NEW] [ ] F - Layered Depth (Product, text, and graphics are on different planes, creating a 3D effect)
SELECTED STYLE: [Choose one based on user request and SELECTED VIBE]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 3: DEFINE VISUAL DESIGN ELEMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Maintain the same viewing angle/camera angle as in the input product image if possible.
[UPDATED] BACKGROUND DESIGN:
--- IF VIBE IS 'MINIMAL & PROFESSIONAL' ---
Premium products → Deep navy/black/charcoal with subtle gradient OR elegant solid color.
Tech products → Clean white/light gray with minimal geometric lines OR a soft gradient.
Lifestyle products → Soft blurred photo-realistic environment OR a warm, neutral color.
Eco products → Natural greens/earth tones OR organic textures (wood, paper).
--- IF VIBE IS 'ENERGETIC & TRENDY' ---
Bold Solid Color: High-contrast, vibrant color (e.g., electric blue, hot pink, sunshine yellow).
Dynamic Gradient: A 2-3 color gradient with a clear directional flow (e.g., diagonal, radial burst).
Abstract Graphic Background: A composition of shapes, lines, and textures.
Duotone Photo: A background lifestyle image rendered in two high-contrast colors.
Paper/Concrete Texture: A gritty, textured background for an edgy feel.
SELECTED BACKGROUND: [Specific color/style with hex code if applicable, based on Vibe]
[UPDATED] COLOR PALETTE:
--- IF VIBE IS 'MINIMAL & PROFESSIONAL' ---
Primary: [subtle, deep, or neutral color]
Accent: [a single contrasting color for CTA]
Supporting: [2-3 analogous or muted colors]
--- IF VIBE IS 'ENERGETIC & TRENDY' ---
Vibrant & Contrasting: 2-3 bold, saturated colors that create high energy.
Monochromatic Punch: Shades of one color plus a single, powerful neon accent.
Retro Revival: A palette inspired by the 70s, 80s, or 90s (e.g., oranges/browns, or pastels/neons).
SELECTED PALETTE: [Define Primary, Accent, and Supporting colors]
[UPDATED] DESIGN ELEMENTS TO INCLUDE:
--- FOR 'MINIMAL & PROFESSIONAL' VIBE ---

Geometric shapes (clean circles/lines)

Subtle gradient overlay

Faint texture (grain/fabric)

Soft light effects (glow/spotlight)

Architectural shadow drama
FOR 'ENERGETIC & TRENDY' VIBE

Abstract Blobs & Shapes: Organic, fluid shapes to frame content.

Hand-drawn Scribbles/Arrows: To add a human, energetic touch.

Dynamic Angled Lines/Speed Lines: To create a sense of motion.

Neon Glow Effect: Applied to text or shapes for a futuristic look.

Paper Tear / Collage Effect: For a layered, scrapbook feel.

Bold Outlined Shapes: To create frames or highlight areas.

Grid or Dot Patterns: A subtle background pattern for a techy feel.

Brush Strokes / Paint Splatters: Adds texture and an artistic flair.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 4: DEFINE TEXT PLACEMENT & TYPOGRAPHY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[UPDATED] TYPOGRAPHY:
--- IF VIBE IS 'MINIMAL & PROFESSIONAL' ---
Headline: Bold sans-serif / Elegant serif / Sleek uppercase.
Brand/CTA: Clean sans-serif.
--- IF VIBE IS 'ENERGETIC & TRENDY' ---
Headline: Expressive Display Font (bold, quirky) / Condensed Impact Sans-Serif / Retro Script.
Brand/CTA: A mix of two complementary fonts (e.g., bold headline, lighter supporting text).
[UPDATED] TEXT PLACEMENT & EFFECTS:
BRAND NAME:
Text: "[exact text]"
Position: [Top left/Top center/Bottom center]
Effects: [None/Subtle shadow]
HEADLINE:
Text: "[exact text]"
Placement Logic:
Minimal: Upper third / Center left / Center right.
Trendy: Angled/Rotated / Stacked Vertically / Partially overlapping product / Integrated into a graphic shape.
Size: Large, prominent
Effects:
Minimal: None / Shadow for depth.
Trendy: Text Outline/Stroke / Gradient Fill / Cut-out Effect (reveals background) / Placed Behind Product.
CALL-TO-ACTION:
Text: "[exact text]"
Style: [Rounded rectangle button / Pill-shaped badge / Minimal underlined text] OR [NEW] [Bold text with a simple arrow icon]
Position: [Bottom right/Bottom center]
Colors & Size: Moderate, clear, and high-contrast.
PROMOTIONAL BADGE/BANNER (if applicable):
Style: [Corner ribbon/Circular badge] OR [NEW] [Starburst / Angled Banner / Loud Sticker Graphic].
Position: [Top right corner] OR [Overlapping product corner].
Colors: Urgent reds/yellows OR bold, on-brand colors.
FOOTER:
Position: Bottom edge, small and subtle.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 5: DEFINE FESTIVE/SEASONAL OVERLAYS (if applicable)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
IF SEASONAL THEME SELECTED IN STEP 2:

CHRISTMAS:

Elements: Warm white string lights draped across top third, red and gold ornament accents in corners, subtle snowflakes overlay, pine branch elements framing edges

Colors: Traditional red, green, gold, white

Placement: Overlaid ON the composition, not obscuring product

NEW YEAR:

Elements: Gold and silver confetti burst, champagne gold accents, celebratory firework graphics, "2024/2025" year elements if relevant

Colors: Midnight blue, champagne gold, silver, black

Placement: Celebratory elements around product, not covering

BLACK FRIDAY/SALES:

Elements: Bold geometric sale badges, lightning bolt graphics, urgent color blocks

Colors: Black, red, yellow, white for high contrast

Placement: Corner badges, side banners

SUMMER:

Elements: Sun ray graphics, tropical leaf accents, bright color pops, beach texture hints

Colors: Bright yellows, oranges, turquoise, coral

Placement: Background elements, corner accents

SPRING:

Elements: Delicate floral corner pieces, soft botanical elements, pastel color accents

Colors: Soft pink, mint green, lavender, cream

Placement: Edge decorative elements

HALLOWEEN:

Elements: Autumn leaves, orange and purple color accents, subtle spooky-fun elements

Colors: Orange, purple, black, deep autumn tones

Placement: Scattered elements, color grade overlay

VALENTINE'S:

Elements: Heart shapes, rose petal accents, romantic color washes

Colors: Deep red, pink, rose gold, white

Placement: Corner accents, subtle background elements

DESCRIBE EXACT FESTIVE ELEMENTS: [Based on theme from Step 2]
This section can be applied to either vibe, though the intensity and style of the elements can be adapted.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
STEP 6: GENERATE THREE UNIQUE PROMPT VARIATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Based on all the analysis and specifications from Steps 1-5, you MUST create THREE DIFFERENT creative variations.
Each variation should maintain the SAME:
- Product description (from Step 1)
- Vibe/target audience (from Step 2)
- Brand name, headline text, CTA text (from Step 2)
- Seasonal theme if applicable (from Step 5)

Each variation MUST DIFFER in:
- Design element approach and composition
- Typography style and text effects
- CTA button/badge design
- Background treatment
- Overall creative execution

VARIATION GUIDELINES:

PROMPT 1 - "GEOMETRIC & COLORFUL"
Focus: Bold geometric shapes, vibrant color blocking, modern abstract design
Design Elements: Use geometric shapes (circles, triangles, rectangles) from product color palette, overlapping layers, color blocks
Typography: Bold, block letters with solid fills or gradient effects
CTA Style: Sharp-edged rectangular button or geometric badge
Creative Direction: High-contrast, shape-driven, modern and structured

PROMPT 2 - "BRAND ESSENCE & THEMED"
Focus: Aligned with brand guidelines, seasonal/festive elements prominent, professional polish
Design Elements: Refined use of brand colors, themed elements (if seasonal), subtle textures, elegant overlays
Typography: Brand-appropriate font (elegant serif for luxury, clean sans-serif for tech), professional spacing
CTA Style: Classic rounded button or pill-shaped badge, on-brand colors
Creative Direction: Cohesive, theme-focused, marketing-ready, adheres closely to specified theme

PROMPT 3 - "EXPERIMENTAL & DYNAMIC"
Focus: Creative risk-taking, unexpected layouts, artistic flair, high engagement potential
Design Elements: Mix of hand-drawn elements, organic shapes, dynamic angles, layered depth, unexpected textures
Typography: Mixed font styles, rotated/angled text, creative text treatments (outlines, shadows, cutouts)
CTA Style: Unconventional - arrow with text, sticker-style callout, or integrated into design element
Creative Direction: Eye-catching, scroll-stopping, pushes creative boundaries while staying on-brand

YOU MUST OUTPUT IN THIS EXACT FORMAT:

prompt 1: "Marketing creative product advertisement image. [VIBE] style - GEOMETRIC & COLORFUL VARIATION.
PRODUCT: [EXACT complete description from Step 1].
COMPOSITION STYLE: [Describe geometric-focused layout].
BACKGROUND: [Bold, colorful background with geometric color blocking].
DESIGN ELEMENTS: [Specific geometric shapes - circles, triangles, rectangles - with exact placement and colors from product palette. E.g., "Large yellow circle in top right, overlapping medium blue triangle in center-left, thin rectangular color block along bottom edge"].
COLOR PALETTE: [Vibrant, high-contrast colors from product palette].
TEXT ELEMENTS - EXACT PLACEMENT & STYLE:
[BRAND NAME if provided]: Brand name text reading "[EXACT TEXT]" at [position], using [bold geometric sans-serif], [size], [color with solid fill].
[HEADLINE if provided]: Headline text reading "[EXACT TEXT]" positioned [location], using [bold block letter font], large prominent size, [color], [solid fill or geometric gradient effect].
Call-to-action reading "[EXACT TEXT]" as a [sharp rectangular button] at [position], with [color] background and [color] text.
[PROMOTIONAL BADGE if provided]: [Geometric badge shape] displaying "[EXACT TEXT]" positioned [location], in [colors].
[SEASONAL ELEMENTS if applicable]: [Describe festive elements integrated with geometric style].
LIGHTING & MOOD: [Bright/dramatic] lighting creating a [modern, energetic, structured] mood.
TECHNICAL: High-resolution commercial advertising quality, photorealistic product rendering, professional graphic design, balanced visual hierarchy, social media marketing ready.
PRESERVE: Exact product appearance from input image. Marketing elements enhance but never alter the product itself."

prompt 2: "Marketing creative product advertisement image. [VIBE] style - BRAND ESSENCE & THEMED VARIATION.
PRODUCT: [EXACT complete description from Step 1].
COMPOSITION STYLE: [Describe brand-aligned, theme-focused layout].
BACKGROUND: [Brand-appropriate background with seasonal/thematic elements if applicable].
DESIGN ELEMENTS: [Refined, theme-appropriate elements. E.g., "Subtle brand-color gradient overlay, delicate snowflake graphics in corners (if Christmas theme), soft textural elements, elegant framing"].
COLOR PALETTE: [Brand colors with seasonal accents if applicable].
TEXT ELEMENTS - EXACT PLACEMENT & STYLE:
[BRAND NAME if provided]: Brand name text reading "[EXACT TEXT]" at [position], using [brand-appropriate font - elegant serif or clean sans-serif], [size], [color].
[HEADLINE if provided]: Headline text reading "[EXACT TEXT]" positioned [location], using [professional, brand-aligned font], large prominent size, [color], [clean treatment with subtle shadow or none].
Call-to-action reading "[EXACT TEXT]" as a [classic rounded rectangle or pill-shaped button] at [position], with [brand color] background and [contrasting color] text.
[PROMOTIONAL BADGE if provided]: [Classic corner ribbon or circular badge] displaying "[EXACT TEXT]" positioned [location], in [brand colors].
[SEASONAL ELEMENTS if applicable]: [Describe festive elements as per Step 5 - e.g., "Warm white string lights draped across top, red and gold ornaments in corners, subtle snowflakes"].
LIGHTING & MOOD: [Professional, polished] lighting creating a [premium, trustworthy, on-brand] mood.
TECHNICAL: High-resolution commercial advertising quality, photorealistic product rendering, professional graphic design, balanced visual hierarchy, social media marketing ready.
PRESERVE: Exact product appearance from input image. Marketing elements enhance but never alter the product itself."

prompt 3: "Marketing creative product advertisement image. [VIBE] style - EXPERIMENTAL & DYNAMIC VARIATION.
PRODUCT: [EXACT complete description from Step 1].
COMPOSITION STYLE: [Describe dynamic, unconventional layout - e.g., "Asymmetrical composition with product at 15-degree angle, layered depth with overlapping elements"].
BACKGROUND: [Creative, unexpected background - e.g., "Duotone gradient with paper texture overlay" or "Abstract brush strokes in product colors"].
DESIGN ELEMENTS: [Artistic, mixed elements. E.g., "Organic blob shapes framing product, hand-drawn arrows pointing to features, neon glow effect on accents, layered paper-tear effect, dynamic speed lines creating motion"].
COLOR PALETTE: [Creative interpretation of product colors - may include unexpected accent or effect].
TEXT ELEMENTS - EXACT PLACEMENT & STYLE:
[BRAND NAME if provided]: Brand name text reading "[EXACT TEXT]" at [position], using [creative font treatment], [size], [color with unique effect - e.g., outline stroke, gradient fill, or placed behind product].
[HEADLINE if provided]: Headline text reading "[EXACT TEXT]" positioned [creative placement - angled/rotated/stacked], using [expressive display font or mixed fonts], large prominent size, [color], [creative treatment - outline stroke, cutout effect, gradient fill, shadow layers].
Call-to-action reading "[EXACT TEXT]" as a [unconventional style - bold text with arrow icon, sticker-style callout, or integrated graphic element] at [position], with [color] and [creative styling].
[PROMOTIONAL BADGE if provided]: [Creative badge - starburst, angled banner, loud sticker graphic] displaying "[EXACT TEXT]" positioned [unexpected location - overlapping product, integrated into design], in [bold colors].
[SEASONAL ELEMENTS if applicable]: [Describe festive elements with creative twist - e.g., "Abstract interpretation of snowflakes as geometric crystals, string lights rendered as neon glow lines"].
LIGHTING & MOOD: [Dynamic, artistic] lighting creating a [energetic, attention-grabbing, innovative] mood.
TECHNICAL: High-resolution commercial advertising quality, photorealistic product rendering, professional graphic design, balanced visual hierarchy, social media marketing ready.
PRESERVE: Exact product appearance from input image. Marketing elements enhance but never alter the product itself."

CRITICAL RULES:
✓ ALL THREE prompts must maintain exact product description from Step 1
✓ ALL THREE prompts must use the same brand name, headline text, and CTA text
✓ ALL THREE prompts must respect the identified VIBE
✓ Each prompt must be DISTINCTLY DIFFERENT in creative execution
✓ Output format MUST be: prompt 1: "..." prompt 2: "..." prompt 3: "..."
✓ Product itself remains unchanged - only marketing elements vary

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINAL OUTPUT REQUIREMENTS - READ CAREFULLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

After completing your analysis in Steps 1-5, you MUST output EXACTLY THREE prompts in this format:

prompt 1: "Marketing creative product advertisement image (For Instagram, social media). [Full detailed prompt for GEOMETRIC & COLORFUL variation following the structure above]"

prompt 2: "Marketing creative product advertisement image (For Instagram, social media). [Full detailed prompt for BRAND ESSENCE & THEMED variation following the structure above]"

prompt 3: "Marketing creative product advertisement image (For Instagram, social media). [Full detailed prompt for EXPERIMENTAL & DYNAMIC variation following the structure above]"

DO NOT include any other text, explanations, or markdown formatting in your final output.
DO NOT use code blocks or formatting markers.
ONLY output the three prompts in the exact format shown above.

BEGIN YOUR RESPONSE BY COMPLETING STEPS 1-5 FOR YOUR OWN ANALYSIS, THEN OUTPUT THE THREE PROMPTS.
"""