"""
Nano Banana Operation Templates
38 operations with example-driven, flexible instruction templates
Each template guides the LLM without restricting creativity
"""

# ===========================
# OPERATION DEFINITIONS
# ===========================

OPERATIONS = {
    1: {
        "id": 1,
        "name": "Multi-Angle Generation",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
You are generating an image editing instruction for Nano Banana AI.

OPERATION: Multi-Angle Product View Generation

GOAL: Create additional viewing angles of the product (front, back, side, top, 45-degree angles)

EXAMPLE APPROACHES:

Example 1 - Side View:
"Generate a 90-degree rotated side view of this product. Maintain exact product dimensions, colors, and all visible branding. Use the same studio lighting from the original image (soft diffused light from top-left). Keep the product centered in the frame against a clean white background. Preserve all texture details and material finishes."

Example 2 - Back View:
"Create a 180-degree rear view showing the back of the product. Maintain all product characteristics including size, color accuracy, and design details. Match the lighting conditions of the original image. Ensure any rear-facing features, ports, or labels are clearly visible and accurately rendered."

Example 3 - Top-Down View:
"Generate a bird's-eye view of the product from directly above. Keep the product centered and properly scaled. Maintain accurate proportions and show all top-surface details clearly. Use consistent lighting that matches the original image's studio setup."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Default to a standard 45-degree side view
- Maintain original lighting conditions
- Keep product at same scale
- Use clean white or matching background
- Preserve all product details exactly

CRITICAL REQUIREMENTS:
- Product dimensions and proportions must remain accurate
- All branding, logos, and text must be preserved
- Colors must match the original product exactly
- Lighting should be consistent with original image
- Background should be clean and non-distracting

Generate a hyper-specific instruction for Nano Banana.
"""
    },
    
    2: {
        "id": 2,
        "name": "Lifestyle / Contextual Placement",
        "category": "All",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: Lifestyle Context Generation

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

USER SPECIFICATIONS:
{user_details}

NOTE:
***Generate the detailed product description from Step 1 and final prompt (Step 3) for the product imgage provided.*** 

"""
    },
    
    3: {
        "id": 3,
        "name": "Close-up / Macro Detail View",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Macro Close-Up for E-Commerce Product Detail

GOAL: Create a zoomed-in view showing product texture, material quality, and craftsmanship details that help customers make informed purchasing decisions.

CRITICAL REQUIREMENT: The zoomed texture must be EXACTLY as it appears in the original image. Do not generate, enhance, or fabricate texture details. Only magnify what actually exists in the source image.

E-COMMERCE CONTEXT:
This close-up will be part of a product listing image set. Customers use detail shots to:
- Verify material quality (stitching, weave, finish, surface treatment)
- Check craftsmanship (precision, build quality, component details)
- Assess authenticity and product condition
- Make confident purchase decisions

INTELLIGENT AREA SELECTION (when user doesn't specify):
Analyze the product image and select the most valuable detail area for e-commerce based on:

Priority 1 - Quality Indicators:
- Stitching quality (for apparel, furniture, bags)
- Material texture (fabric weave, metal finish, wood grain, plastic texture)
- Manufacturing precision (seams, joints, edges, machining marks)
- Brand logos or badges (close-up of embossed/printed branding)

Priority 2 - Unique Features:
- Patented mechanisms or innovative design elements
- Premium materials (leather grain, carbon fiber weave, brushed aluminum)
- Functional details (buttons, zippers, connectors, fasteners)
- Quality certifications or rating labels

Priority 3 - Differentiation Points:
- Elements that distinguish this product from competitors
- High-value components that justify pricing
- Warranty tags or authenticity marks

AVOID These Areas (poor e-commerce value):
- Plain surfaces with no distinctive features
- Generic plastic or smooth metal with no texture
- Areas with glare, shadows, or poor original image quality
- Background or non-product elements

EXAMPLE APPROACHES:

Example 1 - Apparel Product (Jacket):
"Identify the area with the most visible stitching quality - likely a seam, collar, or pocket edge. Zoom to 400% magnification on this stitching detail. Frame the shot to show 3-4 inches of the seam, filling 75% of the image. The stitching thread, fabric weave, and seam precision must appear EXACTLY as in the original photo - same thread color, same stitch spacing, same fabric texture. Use shallow depth of field with the stitching in razor-sharp focus. Apply soft blur (8px) to background fabric for depth. Lighting should enhance visibility without altering the actual appearance."

Example 2 - Electronics (Laptop):
"Locate the most informative port or interface area - typically the side panel with USB-C, HDMI, or charging ports. Zoom to 350% magnification centering on these ports. Fill 80% of frame with the port cluster. Show the exact metal finish, port labeling, and precision of the cutouts as they appear in the original image. No enhancement of details - only magnification. Use clean, even lighting to show port depth and metal finish clearly. Sharp focus on port openings, slight blur (10px) on surrounding chassis."

Example 3 - Furniture (Chair):
"Find the upholstery texture or wood joint that best demonstrates quality. For fabric: zoom 300% on the weave showing fabric density and texture pattern. For wood: zoom on a visible joint or wood grain detail. Frame to show 6x6 inch area of material, filling 70% of frame. Texture must match original image perfectly - same weave pattern, same wood grain, same color and finish. Use angled lighting (45 degrees) to reveal texture depth without creating harsh shadows. Primary detail in sharp focus, edges with gradual 12px blur."

Example 4 - Tools/Industrial (Power Drill):
"Identify the area showing build quality - typically the motor housing seam, grip texture, or brand badge. Zoom 350% on the selected detail. If grip: show the rubber texture pattern exactly as it appears in original. If seam: show how precisely parts fit together. If badge: show embossing depth and text clarity. Fill 75% of frame with the detail. Maintain absolute color accuracy and texture fidelity to original image. Use directional lighting to emphasize three-dimensional aspects of the detail."

Example 5 - Beauty/Cosmetics (Bottle):
"Focus on label details, cap threading, or bottle material finish. Zoom 300% on the most informative area. If label: show text clarity and print quality exactly as original. If cap: show threading precision and material finish. If bottle: show glass/plastic clarity and any embossing. Frame detail to fill 80% of image. Colors, text, and textures must be identical to source image. Lighting should show material quality (reflectivity, transparency, surface finish) clearly."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Use the intelligent area selection priorities above
- Default to 300-400% magnification
- Fill 70-80% of frame with the selected detail
- Ensure the detail has genuine e-commerce value
- Maintain absolute fidelity to original image texture

TECHNICAL EXECUTION REQUIREMENTS:

Magnification & Framing:
- Zoom level: 300-500% depending on detail size
- Frame composition: Detail fills 70-85% of image
- Leave 15-30% as context (slightly blurred surrounding area)

Focus & Depth:
- Primary detail: Razor-sharp focus (0% blur)
- Immediate surrounding: Slight blur (5-8px) for depth
- Background context: Moderate blur (12-20px) to maintain focus on detail

Lighting for Detail Visibility:
- Use directional lighting (30-60 degree angle) to reveal texture depth
- Avoid flat lighting that hides surface details
- Avoid harsh lighting that creates confusing shadows
- Goal: Make texture and quality clearly visible to customers

Color & Texture Accuracy:
- CRITICAL: Texture appearance must match original image exactly
- No AI enhancement or fabrication of details
- No color shifts or saturation changes
- No sharpening artifacts or noise reduction that alters texture
- What's in the original is what's shown - just larger

Professional E-Commerce Standards:
- Image should look professionally photographed
- Detail should be immediately understandable to customers
- Should answer the question: "What is this product made of?"
- Should build confidence in product quality
- No distracting elements or confusing compositions
NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)

Generate a hyper-specific prompt that creates a valuable e-commerce product detail shot from the provided input image.
"""
},
    
    4: {
        "id": 4,
        "name": "360° / Rotational View Generation",
        "category": "Tools, Electronics",
        "test_image_type": "electronics_laptop",
        "instruction_template": """
OPERATION: Rotational/360-Degree View

GOAL: Generate a view showing the product rotated to a different angle

EXAMPLE ROTATIONS:

Example 1 - 90° Rotation:
"Rotate the product 90 degrees clockwise to show the right side panel. Maintain the same eye-level camera position (4 feet from product, 3 feet high). Keep identical studio lighting - key light from top-left, fill light from right at 30% intensity. Product should remain centered and at the same scale. Show all side panel details, ports, and features clearly. Background remains clean white."

Example 2 - 45° Diagonal View:
"Generate a 45-degree rotated view showing both front and right side simultaneously. Camera at slight high angle (10 degrees above eye-level). Maintain all product proportions accurately. Use the same three-point lighting setup. Ensure all visible surfaces are evenly lit. Product centered, filling 65% of frame height."

Example 3 - Slight Rotation for Depth:
"Rotate product 15 degrees counter-clockwise for a more dynamic view. Keep same camera distance and height. Maintain original lighting setup exactly. This subtle rotation should add depth while keeping all front features clearly visible. Scale and proportions must remain accurate."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Default to 45-degree rotation (shows depth)
- Maintain original lighting
- Keep product at same scale
- Preserve all details and colors
- Clean, professional background

REQUIREMENTS:
- Accurate geometric rotation
- Consistent lighting across surfaces
- No distortion or stretching
- All features remain clear

Generate the instruction.
"""
    },
    
    5: {
        "id": 5,
        "name": "Fitment / Exploded View Simulation",
        "category": "Automotive, Industrial, Tools, HVAC, Plumbing",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Intelligent Exploded Assembly View Generation

GOAL: Create a logical, educational exploded view showing how the product is assembled, what components it contains, and how parts fit together.

CRITICAL THINKING REQUIREMENTS:
Before creating the exploded view, analyze the product image and reason through:

1. PRODUCT STRUCTURE ANALYSIS:
   - What is this product's primary function?
   - What internal components would be needed for this function?
   - What is the logical assembly sequence (outside-in or inside-out)?
   - What fasteners or connection methods are likely used?

2. VISIBLE COMPONENT IDENTIFICATION:
   - External casing/housing (usually the largest part to preserve)
   - Visible access panels, covers, or removable parts
   - Control interfaces (buttons, knobs, displays)
   - Connectors, ports, or attachment points
   - Mounting hardware visible in the image

3. LOGICAL INTERNAL COMPONENTS (must reason based on product type):
   - Power source (battery, motor, engine, electrical components)
   - Functional mechanism (gears, pumps, heating elements, cutting blades)
   - Structural frame or chassis
   - Fasteners (screws, bolts, clips, snap-fits)
   - Seals, gaskets, or protective elements

4. ASSEMBLY LOGIC:
   - How would a technician assemble this product?
   - Which parts go together first?
   - What is the logical separation sequence for maximum clarity?

CRITICAL PRESERVATION REQUIREMENT:
The OUTER SHELL/CASING must remain complete and recognizable. Do not fragment, alter, or distort the main housing. Show it as one cohesive piece with other components separated from it.

EXPLODED VIEW PRINCIPLES:

Separation Strategy:
- Separate components along natural assembly axes (vertical, horizontal, or radial)
- Maintain logical spatial relationships (parts stay aligned with their mounting positions)
- Create clear visual gaps (2-6 inches between major components)
- Preserve component orientation (parts should look ready to slide back into place)

Alignment & Positioning:
- Use a consistent explosion axis (typically straight up, or along product's main axis)
- Keep components aligned on their assembly path
- Spacing should be proportional to component size
- Larger components: 4-6 inch separation
- Smaller components: 2-3 inch separation
- Hardware (screws, bolts): 1-2 inch separation, grouped logically

Visual Hierarchy:
- Main housing: Most prominent, usually bottom or center
- Primary mechanism: Separated but clearly related to housing
- Secondary components: Logically positioned around primary
- Hardware/fasteners: Grouped and positioned near their mounting points

LABELING & ANNOTATION SYSTEM:

Connection Lines:
- From each separated component: Draw a thin, clean line (1-2px) to its text label
- Line should originate from the component's center or most recognizable feature
- Line travels to the label WITHOUT crossing the product or other components
- Line style: Solid or dashed, in contrasting color (dark gray on light bg, white on dark bg)
- Line ends: Small circle or dot at component, arrow or plain end at label

Label Positioning:
- Arrange labels in organized columns on LEFT or RIGHT side of the exploded view
- Leave minimum 2 inches clearance from all product components
- Align labels vertically with consistent spacing (0.5-1 inch between labels)
- Connect each label to its component with the connection line

Label Content:
- Component name (e.g., "Housing Cover", "Motor Assembly", "Battery Pack")
- Optional: Part number or brief description in smaller text below
- Font: Arial or Helvetica, Bold for component name, Regular for description
- Size: 12-14pt for name, 9-10pt for description
- Color: High contrast with background

Numbering System (optional but professional):
- Number each component (1, 2, 3...) in assembly sequence
- Place number in a small circle on or near each component
- Match numbers in the label list
- Format: "1. Main Housing", "2. Motor Mount", etc.

EXAMPLE APPROACHES:

Example 1 - Power Tool (Drill):
"Analyze: This is a cordless drill. Core components likely include: outer housing (handle + body), electric motor, gear transmission, battery pack, trigger mechanism, chuck assembly.

Exploded view composition:
- MAIN HOUSING (handle + body shell): Keep as ONE complete piece, positioned at bottom-center. This is the reference point. Preserve exactly as shown in original image - all colors, branding, shape.
- BATTERY PACK: Separate 4 inches BELOW the housing, aligned with handle grip area where it normally mounts. Draw thin gray connection line from battery to label 'Battery Pack (20V Li-ion)' positioned in right column.
- MOTOR ASSEMBLY: Separate 3 inches ABOVE the housing, positioned where motor cavity would be. Show cylindrical motor with shaft. Connection line to label 'Electric Motor'.
- GEAR TRANSMISSION: Separate 4 inches ABOVE motor, aligned with front of tool. Show gear housing. Line to label 'Planetary Gear System'.
- CHUCK ASSEMBLY: Separate 5 inches ABOVE gears, at the front. Show chuck mechanism. Line to label 'Keyless Chuck'.
- TRIGGER & SWITCH: Separate 2 inches to the RIGHT of main housing. Line to label 'Variable Speed Trigger'.
- SCREWS (4-6 visible): Separate 2 inches to LEFT of housing, grouped together. Single line to label 'Housing Screws (6x)'.

All components aligned vertically along the drill's central axis. Labels organized in right column with consistent spacing. Connection lines in dark gray (#4A5568), clean and professional. Background remains clean. The exploded view clearly shows assembly sequence: screws hold housing → motor fits inside → gears connect to motor → chuck attaches to gear output → battery slides into handle → trigger controls motor."

Example 2 - Kitchen Appliance (Blender):
"Analyze: Blender consists of: base housing with motor, blade assembly, jar/pitcher, lid, control panel.

Exploded vertical stack (bottom to top):
- BASE HOUSING: Bottom position, complete and unchanged. All buttons, branding visible. 
- MOTOR (internal): Separate 3 inches ABOVE base, shown as cylindrical unit with shaft pointing up. Line to right label 'Motor Assembly (800W)'.
- COUPLING MECHANISM: 2 inches above motor. Small gear/coupling piece. Line to label 'Blade Coupling'.
- BLADE ASSEMBLY: 3 inches higher. Show blade unit with sealing gasket. Line to label 'Stainless Steel Blade Assembly'.
- PITCHER JAR: 4 inches above blades. Transparent pitcher showing it would sit on blade assembly. Line to label 'Glass Pitcher (64 oz)'.
- LID: 3 inches above pitcher. Show lid with center cap. Line to label 'Lid with Measuring Cap'.

Labels in right column, aligned vertically. Connection lines do not cross components. Assembly logic clear: base → motor inside → coupling on motor shaft → blades screw onto coupling → pitcher sits on blade assembly → lid closes pitcher."

Example 3 - Automotive Part (Car Alternator):
"Analyze: Alternator components include: front/rear housing, rotor, stator, voltage regulator, pulley, bearings, brushes.

Horizontal explosion (left to right):
- REAR HOUSING: Left position, complete with visible mounting brackets. Preserve exactly.
- VOLTAGE REGULATOR: 2 inches to RIGHT of rear housing, shows circuit board. Line to label positioned above.
- BRUSH ASSEMBLY: 1.5 inches right of regulator. Small component with carbon brushes visible.
- STATOR: 3 inches right of brushes. Circular component with copper windings visible.
- ROTOR: 3 inches right of stator. Cylindrical with magnetic poles, shaft extending through.
- FRONT HOUSING: 2 inches right of rotor. Shows bearing seat.
- PULLEY & FAN: 3 inches right of front housing. Pulley with cooling fan behind it.
- BEARINGS (2): Separated small components, positioned near front/rear housing with lines to labels.
- THROUGH-BOLTS (4): Positioned top and bottom, with lines to label 'Through Bolts (4x)'.

Labels organized above and below main components. All components aligned horizontally showing clear assembly path. Connection lines in white (assuming dark/mechanical background). Professional technical manual aesthetic."

Example 4 - HVAC Component (Thermostat):
"Analyze: Thermostat consists of: wall plate, main body, display module, circuit board, wire terminals, mounting screws.

Perpendicular explosion (away from wall):
- WALL PLATE: Positioned at back (appears flat against wall). Complete with screw holes and wire pass-throughs visible.
- MAIN BODY HOUSING: 2 inches FORWARD from wall plate. Shows internal cavity, preserved completely.
- CIRCUIT BOARD: 3 inches forward from body. Flat PCB with visible components, wire terminals on edge.
- DISPLAY MODULE: 2 inches forward from circuit board. LCD screen with ribbon cable connection.
- FRONT COVER: 3 inches forward from display. Outer shell with brand logo and button cutouts.
- WIRE TERMINALS: Separated 2 inches to the LEFT of wall plate. Bundled terminal block with colored wire indicators (R, W, G, Y, C).
- MOUNTING SCREWS (2): 2 inches to the RIGHT of wall plate.

Labels positioned in left and right columns. Lines connect clearly to each component. View shows how thermostat assembles onto wall: plate screws to wall → wires connect to terminals → body clips onto plate → circuit board inserts → display connects → cover snaps on. Clean, instructional quality."

Example 5 - Plumbing Fixture (Faucet):
"Analyze: Faucet components: spout body, handle, cartridge/valve, mounting hardware, aerator, supply connections.

Vertical explosion (top to bottom):
- HANDLE: Top position. Lever or knob handle preserved exactly.
- HANDLE SCREW & CAP: 1.5 inches below handle. Small parts grouped.
- CARTRIDGE/VALVE: 2 inches below. Cylindrical valve cartridge showing ceramic discs or internal mechanism.
- SPOUT BODY: 3 inches below cartridge. Main faucet body, complete with all chrome finish and curves preserved. This is the main visual reference.
- AERATOR: 1.5 inches below spout tip. Small screened component that screws into spout end.
- O-RINGS/SEALS (2-3): Positioned to the left of spout body, 2 inches away. Grouped small rubber rings.
- MOUNTING NUT: Below spout body, 2 inches down. Large hex nut that secures faucet to sink.
- SUPPLY LINES (2): Separated below mounting nut. Flexible hoses with connectors.

Labels in right column. Each component has clean connection line. Shows assembly: supply lines connect → mounting nut secures from below → spout body is main piece → o-rings seal → cartridge inserts into body → handle attaches to cartridge → aerator screws into spout tip. Professional plumbing diagram quality."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Analyze product category and function to determine logical components
- Create 4-8 separated components (don't over-complicate)
- Use vertical explosion for tall products, horizontal for wide products
- Label major components clearly with professional naming
- Ensure assembly logic is immediately understandable

VISUAL EXECUTION REQUIREMENTS:

Spatial Organization:
- Clear explosion axis (vertical, horizontal, or radial)
- Consistent spacing progression
- Components aligned on assembly path
- No random floating parts

Component Rendering:
- Each separated part maintains its original appearance
- Proportions accurate relative to complete product
- Colors, textures, finishes preserved exactly
- No distortion or stretching

Connection Lines:
- Thin (1-2px), professional appearance
- High contrast with background (dark on light, light on dark)
- Straight or gently curved (no sharp bends)
- Each line connects ONE component to ONE label
- Lines do not cross components or each other when possible

Labels:
- Organized in columns (left, right, or both)
- Consistent font and sizing
- High readability
- Aligned and evenly spaced
- Clear association with components via connection lines

Professional Standards:
- Technical manual quality
- Educational and informative
- Assembly sequence is logical
- Could be used for actual assembly/disassembly reference

Background:
- Clean and uncluttered
- Neutral color that provides contrast
- No distracting elements

NEVER DO:
- Fragment or distort the main housing/casing
- Create random part separations without logic
- Position parts in confusing or ambiguous locations
- Overlap labels with components
- Use illegible connection lines or labels
- Show impossible or illogical assembly sequences
- Omit major visible components
- Add components that don't make sense for product type

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific exploded view prompt that demonstrates logical product structure and clear assembly relationships for the provided product in the image.
"""
    },
    
    6: {
        "id": 6,
        "name": "Virtual Mannequin / Model Fitting",
        "category": "Apparel, Fashion",
        "test_image_type": "apparel_tshirt",
        "instruction_template": """
OPERATION: Mannequin/Model Fitting Visualization

GOAL: Show apparel on a mannequin or model form

EXAMPLE APPROACHES:

Example 1 - Neutral Mannequin:
"Place this garment on a neutral grey mannequin form (gender-neutral torso). Mannequin should be facing forward, standing upright. Show natural fabric drape at shoulders, chest, and hem. Maintain all garment details - seams, logos, patterns, colors exactly as original. Position mannequin centered in frame. Use soft studio lighting from 45-degree angle. Clean white background."

Example 2 - Model Visualization:
"Visualize this clothing item on a fashion model (appropriate gender for garment). Model in neutral standing pose (arms slightly away from body). Show realistic fabric drape and fit. Maintain 100% accurate garment appearance - no color changes, pattern alterations, or detail modifications. Model should enhance garment presentation without distracting. Natural skin tone, minimal makeup, simple hairstyle. Studio lighting setup."

Example 3 - Flat Lay to Worn:
"Transform this flat product image into a worn visualization on a form. Show how the garment naturally drapes on a human body shape. Preserve all fabric textures, prints, and details exactly. Display proper garment proportions when worn (shoulders, waist, length). Use appropriate body form size for garment size. Clean presentation."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Use neutral grey mannequin
- Show natural, realistic drape
- Maintain all garment details 100%
- Professional fashion photography style
- Clean background

REQUIREMENTS:
- Garment appearance unchanged (color, pattern, texture)
- Realistic fit and drape
- Professional presentation
- Focus remains on garment

Generate the instruction.
"""
    },
    
    7: {
        "id": 7,
        "name": "Dimension & Scale Visualization",
        "category": "Furniture, Tools",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: Professional Dimension Overlay for E-Commerce

GOAL: Add accurate, professional dimension lines and measurements to help customers understand product size.

CRITICAL REQUIREMENTS:
1. NEVER overlay dimension text or lines directly on the product itself
2. Position ALL dimension indicators OUTSIDE the product boundaries
3. Use contrasting colors based on background (dark on light, light on dark)
4. Maintain professional technical drawing standards
5. Measurements must be accurate or clearly marked as approximate
6. Maintain absolute product fidelity. Instruct the model to maintain and preserve the product. NO duplicate overlays allowed.
7. Do not alter the product in the image in any way. DO not invent any new features.

COLOR & CONTRAST RULES:

Analyze Background Color:
- Light backgrounds (white, cream, light gray, pastels): Use dark dimension graphics
  → Lines: Dark gray (#2D3748) or black (#000000), 2-3px thickness
  → Text: Black (#000000) or dark gray (#1A202C), bold font
  → Arrows/caps: Matching dark color
  
- Dark backgrounds (black, dark gray, navy, dark wood): Use light dimension graphics
  → Lines: White (#FFFFFF) or light gray (#E2E8F0), 2-3px thickness
  → Text: White (#FFFFFF), bold font
  → Arrows/caps: Matching light color

- Medium/mixed backgrounds: Use dual approach
  → Add subtle background panel behind text (semi-transparent: 85% opacity)
  → Dark text on light panel OR light text on dark panel
  → Example: White text on dark gray panel (rgba(0,0,0,0.85))

DIMENSION LINE PLACEMENT (CRITICAL - NO PRODUCT OVERLAP):

Width Dimension (Horizontal):
- Position: ABOVE the product, minimum 2 inches clearance from product's top edge
- Line length: Spans the full width of the product
- End caps: Perpendicular lines (0.5 inch tall) at each end, pointing toward product
- Alignment: Perfectly horizontal, parallel to product's width
- Extension lines (optional): Thin vertical dashed lines (1px, 50% opacity) from product edges up to dimension line

Height Dimension (Vertical):
- Position: To the RIGHT of the product, minimum 2 inches clearance from product's right edge
- Line length: Spans the full height of the product
- End caps: Perpendicular lines (0.5 inch wide) at each end, pointing toward product
- Alignment: Perfectly vertical, parallel to product's height
- Extension lines (optional): Thin horizontal dashed lines (1px, 50% opacity) from product edges to dimension line

Depth Dimension (if needed):
- Position: Bottom-left or top-right diagonal
- Use angled dimension line (typically 30-45 degrees)
- Clear of product with minimum 1.5 inch clearance
- Label clearly as "Depth:" to distinguish from width/height

TEXT LABEL POSITIONING (CRITICAL - NO PRODUCT OVERLAP):

Placement Rules:
- Width measurement: Centered ABOVE the horizontal dimension line
- Height measurement: Centered beside the vertical dimension line (on the right side)
- Minimum distance from product: 2 inches (no exceptions)
- Text should float in empty space, never touching product

Text Background Panel (for readability):
- If text might be hard to read: Add rectangular background panel
- Panel: 120% of text width, 140% of text height
- Panel color: Semi-transparent contrasting color (80-90% opacity)
- Panel has subtle border: 1px, matching dimension line color
- Text centered within panel

EXAMPLE APPROACHES:

Example 1 - Light Background Product (White/Cream):
"Product is on white background. Add dimension lines in dark gray (#2D3748). 

WIDTH dimension: Draw horizontal line 2.5 inches ABOVE product's top edge, spanning exact product width from left edge to right edge. Line thickness: 3px. Add perpendicular end caps (0.5 inch tall, pointing down toward product). Center the text '{width_inches} inches' or '{width_cm} cm' in black Arial Bold 16pt, positioned 0.75 inches ABOVE the dimension line. Text has a subtle white semi-transparent background panel (90% opacity, 1px dark gray border) for maximum clarity.

HEIGHT dimension: Draw vertical line 2.5 inches to the RIGHT of product's right edge, spanning exact product height from top to bottom. Line thickness: 3px. Add perpendicular end caps (0.5 inch wide, pointing left toward product). Position text '{height_inches} inches' in black Arial Bold 16pt, 1 inch to the right of the dimension line, vertically centered. Text on white semi-transparent panel (90% opacity).

Product itself: Completely unchanged, no overlays whatsoever."

Example 2 - Dark Background Product (Black/Charcoal):
"Product is on dark gray background. Use white dimension graphics (#FFFFFF).

WIDTH dimension: Position horizontal line 3 inches ABOVE the product, spanning full width. Line: 2.5px white stroke. Perpendicular end caps at both ends (0.5 inch tall). Text '{width}\"' in white Arial Bold 18pt, positioned 0.75 inches above the dimension line, centered horizontally. Text has dark semi-transparent background panel (rgba(0,0,0,0.85), 1px white border).

HEIGHT dimension: Position vertical line 3 inches to the RIGHT of product. Line: 2.5px white stroke. End caps (0.5 inch wide). Text '{height}\"' in white Arial Bold 18pt, 1.25 inches to the right of the line. Dark panel background for text.

All dimension graphics clearly visible against dark background. Product area: pristine, no overlays."

Example 3 - User Provides Specific Measurements:
"User specified: Width = 24 inches, Height = 36 inches, Depth = 18 inches.

Draw WIDTH dimension line 2 inches above product top edge. Span exactly from left edge to right edge of product. Dark gray line (3px) with end caps. Label: '24 inches' or '24\"' in Arial Bold 16pt, positioned above line, centered. Text color matches line color.

Draw HEIGHT dimension line 2.5 inches to right of product. Span from bottom edge to top edge. Same line style. Label: '36 inches' positioned to the right of line, centered vertically.

Draw DEPTH dimension as diagonal line from bottom-left, angled 35 degrees, length representing depth proportion. Label: 'Depth: 18 inches' positioned at end of diagonal line.

Use contrasting colors based on background brightness. ALL dimensions positioned OUTSIDE product boundaries with clear spacing."

Example 4 - No Measurements Provided (Use Placeholders):
"No specific measurements provided. Analyze product proportions visually.

Add dimension lines as professional placeholders:
- WIDTH line above product: Label as 'W: [specify width]' 
- HEIGHT line beside product: Label as 'H: [specify height]'

OR estimate based on product category:
- If chair: Typical width 18-24\", height 30-40\"
- If table: Typical width 48-72\", height 28-30\"
- If tool: Indicate in inches or cm based on apparent size

Use clear, professional dimension line formatting. Position all graphics OUTSIDE product area with minimum 2 inch clearance."

Example 5 - Multiple Dimensions with Extension Lines:
"Create technical drawing style with extension lines.

From product's left and right edges: Draw thin vertical dashed lines (1px, gray, 40% opacity) extending UPWARD 2.5 inches beyond the product. These are extension lines showing where width is measured.

Between these extension lines, 2.5 inches above product: Draw solid horizontal dimension line (3px, dark color) with arrow end caps. Label centered above.

From product's top and bottom edges: Draw thin horizontal dashed lines extending RIGHTWARD 3 inches. 

Between these extension lines, 3 inches to the right: Draw solid vertical dimension line with arrow caps. Label positioned beside.

Professional CAD/technical drawing aesthetic. Product itself untouched."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Use product category to estimate typical dimensions
- OR use placeholder labels: 'Width: [X]\"', 'Height: [Y]\"'
- OR add generic scale reference (human silhouette at 15% opacity in far background)
- Position dimensions professionally with proper clearance

MEASUREMENT UNITS:
- Default to inches for US market: '24\"' or '24 inches'
- Use cm/mm for international: '61 cm' or '610 mm'
- If user specifies units, use those
- Be consistent - don't mix units

LINE STYLE SPECIFICATIONS:

Main Dimension Lines:
- Thickness: 2-3px for visibility
- Style: Solid (not dashed)
- Color: High contrast with background
- Ends: Perpendicular caps (0.4-0.6 inch) or small arrows

Extension Lines (optional):
- Thickness: 1px
- Style: Dashed or dotted (dash: 4px, gap: 3px)
- Color: 30-50% opacity of main line color
- Purpose: Show measurement reference points clearly

TEXT SPECIFICATIONS:

Font: Arial Bold or Helvetica Bold (sans-serif, professional)
Size: 14-18pt (readable but not dominating)
Color: High contrast, matches dimension line color
Background panel: Optional but recommended for clarity
  - Color: Contrasting semi-transparent (80-90% opacity)
  - Padding: 3-5px around text
  - Border: 1px, matching dimension line color

PROFESSIONAL STANDARDS:

Accuracy:
- If measurements provided: Use exact values
- If estimated: Make reasonable estimates or use placeholders
- If uncertain: Use bracketed placeholders [width] to indicate approximation

Clarity:
- Dimensions immediately understandable
- No ambiguity about what's being measured
- Clear visual connection between line and product edge

Aesthetics:
- Clean, technical drawing appearance
- Not cluttered or busy
- Enhances product presentation
- Professional enough for product catalog or technical documentation

NEVER DO:
- Overlay dimensions on the product itself
- Use colors that blend into background (no contrast)
- Place text that obscures product features
- Use illegible font sizes (too small < 12pt)
- Create confusing or ambiguous dimension indicators
- Add dimensions that appear inaccurate or arbitrary

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific prompt that creates professional, accurate dimension overlays positioned OUTSIDE the product boundaries for the image provided.
"""
    },

    8: {
        "id": 8,
        "name": "Material & Finish Simulation",
        "category": "Tools, Furniture, Automotive, Jewelry, Apparel",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Physically-Accurate Material & Surface Finish Transformation

GOAL: Transform the product's surface material or finish while maintaining complete physical realism - accounting for how the new material interacts with lighting, reflections, and the environment.

CRITICAL PHYSICS PRINCIPLE:
Materials interact with light differently. When you change material, you MUST change how light behaves:
- Glossy surfaces create specular highlights and reflections
- Matte surfaces diffuse light evenly with minimal reflections
- Metallic surfaces reflect environment and have colored reflections
- Transparent/translucent materials transmit and refract light
- Textured surfaces create micro-shadows and light scattering

This is NOT just a color change - it's a complete physics simulation of material properties.

MATERIAL PHYSICS UNDERSTANDING:

REFLECTIVITY (How light bounces):
- Mirror finish (chrome, polished metal): 80-95% specular reflection, sharp reflections
- High gloss (lacquer, polished plastic): 60-80% specularity, clear but softer reflections
- Semi-gloss (satin finish): 30-50% specularity, diffused reflections
- Matte (rubber, unfinished wood): 5-15% specularity, mostly diffuse reflection
- Flat (chalk, fabric): 0-5% specularity, pure diffuse reflection

LIGHT INTERACTION CHANGES:
When material changes from matte plastic → glossy metal:
- Highlights become sharper and brighter (increase intensity 50-80%)
- New reflections appear showing environment/surroundings
- Shadow edges may sharpen (less light scatter)
- Color may shift (metals have colored reflections: gold=warm, steel=cool, copper=orange-tint)

When material changes from glossy → matte:
- Existing sharp highlights soften and spread (decrease intensity 40-60%)
- Specular reflections disappear or blur significantly
- Surface appears more uniform in tone
- Shadows may soften slightly (more light scatter)

When material changes from smooth → textured:
- Micro-shadows appear in texture valleys
- Highlights fragment across texture peaks
- Light scatters more (slight overall brightening in shadows)
- Surface appears less uniform, more complex

ENVIRONMENTAL REFLECTION SIMULATION:

Metallic/Glossy Surfaces Need Environment Reflections:
- Chrome/polished metal: Reflect surroundings (if white background, show subtle white/gray reflections)
- Brushed metal: Anisotropic reflections (directional streaks based on grain direction)
- Colored metals: Tint reflections (gold adds warmth, copper adds orange, brass adds yellow)
- Glossy paint: Reflect environment softly, blurred compared to bare metal

Matte Surfaces Have Minimal Reflections:
- Rubber: No environment reflection, uniform appearance
- Fabric: Slight sheen in highlights but no clear reflections
- Unfinished wood: Directional grain pattern but minimal reflection
- Matte paint: Flat appearance, no environmental cues

LIGHTING RESPONSE ADJUSTMENTS:

Analyze Original Lighting:
- Identify light source direction (where are current highlights?)
- Identify shadow positions and hardness
- Note any existing reflections or specular highlights

Adapt for New Material:
- Glossy materials: Increase highlight intensity, make smaller and sharper
- Matte materials: Decrease highlights, spread them out, soften edges
- Metallic materials: Add environmental reflections aligned with light direction
- Textured materials: Add micro-detail in lighting (small highlights on texture peaks)

EXAMPLE TRANSFORMATIONS:

Example 1 - Plastic to Brushed Aluminum:
"Current material: Matte black plastic with minimal reflections and soft highlights.

Target material: Brushed aluminum (horizontal grain).

Physical changes required:
- Base color: Change to metallic gray (RGB: 180, 185, 188) with slight cool blue undertone
- Grain texture: Add horizontal directional lines (0.2mm spacing) across ALL surfaces
- Reflectivity: Increase from 10% to 65% specularity
- Highlights: Original soft highlights → Sharp, elongated horizontal streaks (anisotropic reflection following grain direction)
- New reflections: Add subtle environmental reflections showing ambient lighting, stretched horizontally by grain
- Existing shadows: Maintain positions but slightly sharpen edges (metal scatters less light than plastic)
- Light interaction: Where light hits directly, show bright horizontal streaks; where indirect, show subtle directional sheen

Lighting analysis: Original image has top-left key light creating highlight on upper surface. For aluminum: Create bright horizontal streak across that same upper surface, 70% brighter than original plastic highlight, 3x narrower, perfectly horizontal regardless of surface angle. Add subtle reflection of the background environment (if white bg, show faint white-to-gray gradient reflection on curved surfaces).

Preserve: Exact product shape, all logos/text (but now appear embossed/engraved in metal), all edges and contours, button positions."

Example 2 - Glossy Paint to Soft-Touch Rubber:
"Current material: High-gloss red paint with sharp specular highlights and clear reflections.

Target material: Soft-touch rubberized coating (matte).

Physical changes required:
- Base color: Maintain similar red hue but reduce saturation by 15% (rubber appears less vivid than gloss paint)
- Reflectivity: Decrease from 75% to 8% specularity
- Highlights: Original sharp, bright highlights (90% white intensity) → Broad, subtle highlights (25% intensity, 4x larger area)
- Reflections: Remove all environmental reflections completely (rubber doesn't reflect environment)
- Surface appearance: Add very fine micro-texture (0.1mm grain) suggesting rubberized feel
- Shadows: Slightly soften shadow edges (matte surfaces scatter more light into shadow areas, lift shadow value by 10%)

Lighting analysis: Original has sharp white highlight on top surface from overhead light. For rubber: Spread this highlight into a broad, gentle lightening of the entire top surface, no sharp edges, peak brightness only 25% toward white instead of 90%. The light wrap-around increases - side surfaces receive 15% more light than in glossy version due to subsurface scattering.

Preserve: Product geometry exactly, all surface details, seams, button locations, brand text (now appears pad-printed on rubber rather than glossy)."

Example 3 - Matte Fabric to High-Gloss Lacquer:
"Current material: Matte woven fabric with visible textile texture and no reflections.

Target material: Automotive-grade glossy lacquer (wet look).

Physical changes required:
- Remove fabric weave texture completely → Perfectly smooth surface
- Base color: Maintain color but increase saturation by 25% (gloss enhances color depth)
- Reflectivity: Increase from 5% to 85% specularity
- New highlights: Add sharp, bright specular highlights at every surface that faces the light source, 80-90% white intensity, small and well-defined
- Environmental reflections: Add blurred reflection of surroundings (ceiling, background elements) on curved surfaces, 30-40% opacity
- Depth perception: Gloss creates appearance of depth - add very subtle color gradient (darker in areas facing away from light, 10-15% darker)
- Shadow interaction: Shadows from gloss surfaces are sharper - increase shadow edge definition by 30%

Lighting analysis: Fabric had broad, even illumination with no hotspots. Lacquer version: Add 4-6 distinct specular highlights where surface normal aligns with light source angle. Main highlight on top surface: sharp, 10mm diameter, 85% white. Secondary highlights on curved edges. Add faint reflection of the white background on the glossy surface (white-to-color gradient, 25% opacity).

Preserve: Product form, seams (now appear as panel gaps in lacquer), stitching lines become subtle panel break lines, overall shape exact."

Example 4 - Smooth Plastic to Wood Grain:
"Current material: Smooth injection-molded plastic, slight satin finish.

Target material: Natural oak wood with visible grain and matte polyurethane finish.

Physical changes required:
- Add wood grain pattern: Directional grain lines following product's geometry, 1-3mm spacing, natural variation in width and color (10-15% value variation between grain lines and wood body)
- Base color: Shift to natural oak tone (warm brown, RGB: 160, 120, 80 base with variation)
- Texture: Add fine wood texture with subtle grain ridges (creates micro-shadows in cross-lighting)
- Reflectivity: Adjust to 25% specularity (matte poly finish)
- Highlights: Original highlights → Broader, softer, with slight directional quality following wood grain
- Light scattering: Wood is slightly translucent in thin sections - where edges are thin, add 5-10% warm glow (subsurface scattering simulation)
- Natural variation: Wood has natural color variation - create subtle patches of lighter/darker areas (realistic growth ring patterns)

Lighting analysis: Original plastic had uniform light response. Wood version: Light hitting across grain creates subtle linear highlight streaks following grain direction. Where light hits parallel to grain, highlights are softer and more diffused. Add micro-shadows in grain valleys (2-3% darker than peaks). Edges of product, where wood would be end-grain, show different texture pattern (perpendicular grain lines).

Preserve: Product dimensions exactly, all mounting holes/screw positions (now appear as wood plugs or countersunk), overall industrial design, functional features."

Example 5 - Metal to Carbon Fiber Weave:
"Current material: Brushed stainless steel with directional grain.

Target material: Glossy carbon fiber with visible 2x2 twill weave pattern.

Physical changes required:
- Replace directional metal grain with distinctive carbon fiber 2x2 twill pattern (checkerboard-like weave of fiber bundles, each bundle 3-4mm wide)
- Base color: Deep black with subtle dark gray weave pattern
- Reflectivity: Maintain high specularity (80%) but change reflection character from metallic to glossy resin
- Weave pattern reflections: Each bundle in the weave catches light slightly differently - create alternating highlight pattern where one direction of weave is bright, perpendicular direction is darker
- Depth illusion: Carbon fiber has depth - add very subtle shadow in weave valleys (2-3% darker), highlights on weave peaks
- Reflections: Change from cool metallic reflections to neutral glossy reflections (remove blue tint, add pure environmental reflection)

Lighting analysis: Original metal had horizontal grain highlights. Carbon fiber: Create checkerboard highlight pattern where fiber bundles running perpendicular to light show bright highlights, parallel bundles show darker. Main highlight area shows woven texture clearly with alternating bright/dark bundles (60% bright, 40% less bright in pattern). Curved surfaces show how weave pattern follows product geometry (pattern curves with surface).

Preserve: Product shape exactly, all edges, curves, mounting points, functional elements."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Choose material transformation that enhances product appeal
- Default to common upgrades: plastic→metal, matte→gloss, smooth→textured
- Maintain product's functional appearance (don't make tools look like silk)
- Select material appropriate to product category

TECHNICAL EXECUTION CHECKLIST:

Geometry Preservation:
- Product shape: 100% unchanged
- All edges, curves, contours: Exact
- Buttons, ports, features: Positions unchanged
- Scale and proportions: Identical

Material Properties:
- Base color: Accurate for new material
- Reflectivity: Physically correct specularity level
- Texture: Appropriate detail and pattern
- Finish: Consistent across entire product (or intentionally varied)

Lighting Interaction:
- Highlights: Repositioned and resized based on new material reflectivity
- Intensity: Adjusted for material specularity (brighter for glossy, dimmer for matte)
- Reflections: Added for glossy/metallic, removed for matte
- Shadow response: Adjusted for material light-scattering properties

Environmental Reflections (for glossy/metallic only):
- Show subtle reflection of surroundings
- Reflection clarity matches material (sharp for chrome, soft for satin)
- Reflection color tinted by material (gold=warm, steel=cool)
- Reflection positioned accurately based on viewing angle

Physical Realism:
- Material behaves like real material under the existing lighting
- No impossible physics (matte rubber doesn't have mirror reflections)
- Texture patterns follow product geometry naturally
- Lighting response is consistent across all surfaces

Professional Quality:
- Transformation looks photographed, not computer-generated
- Material choice makes sense for product type
- Result could pass as real product variant
- No obvious artifacts or unrealistic elements

NEVER DO:
- Change product shape or geometry
- Apply material that defies physics (glowing matte surfaces, mirror-finish fabric)
- Keep old material's lighting with new material (matte with sharp highlights)
- Ignore environmental reflections on glossy/metallic surfaces
- Make material look painted-on rather than integral
- Create texture patterns that ignore product geometry (grain goes random directions)
- Keep shadows unchanged when material reflectivity changes significantly

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific prompt that creates a physically-accurate, photorealistic material transformation with proper light interaction simulation.
"""
    },

    9: {
        "id": 9,
        "name": "Fabric / Color Simulation",
        "category": "Apparel, Furniture",
        "test_image_type": "apparel_tshirt",
        "instruction_template": """
OPERATION: Color and Pattern Variation

GOAL: Create color or pattern variants of the product

EXAMPLE VARIATIONS:

Example 1 - Solid Color Change:
"Change the product's primary color to navy blue (Hex: #001F3F). Maintain the same fabric texture, weave pattern, and light interaction. Keep highlights and shadows in the same positions, only shifting the hue. Preserve all seams, stitching, logos, and labels in their original colors. The saturation level should match the original image. All other elements (buttons, zippers, tags) remain unchanged."

Example 2 - Pattern Preservation:
"Change the base color to forest green (Hex: #228B22) while keeping the existing stripe pattern visible. The pattern maintains its contrast relationship with the new base color. Preserve fabric texture appearance and light reflections. All structural details like seams and folds remain identical. Only the color palette shifts, pattern geometry stays exact."

Example 3 - Multi-Color Variant:
"Create a two-tone version: change the main body to charcoal grey (Hex: #36454F), keep accent panels in the original red. Maintain clear boundaries between color zones. Preserve all fabric texture, wrinkles, and lighting effects. The color transition should look natural and professionally dyed. All logos and branding unchanged."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Choose a complementary color that enhances the product
- Maintain fabric texture and light interaction
- Keep all non-color elements (logos, stitching) unchanged
- Professional product photography quality
- Realistic color rendering

REQUIREMENTS:
- Only color/pattern changes, no shape alterations
- Texture and material appearance preserved
- Lighting and shadows remain consistent
- Realistic and professionally executed

Generate the instruction.
"""
    },

    10: {
        "id": 10,
        "name": "Port / Interface Highlighting",
        "category": "Electronics",
        "test_image_type": "electronics_laptop",
        "instruction_template": """
OPERATION: Port and Interface Element Highlighting

GOAL: Visually highlight ports, buttons, and interface elements

EXAMPLE HIGHLIGHTING METHODS:

Example 1 - Colored Circles with Labels:
"Highlight each port and button with thin colored circles (2px stroke, no fill). Use distinct colors: USB ports = blue (#0078D4), power button = green (#10B981), audio jack = purple (#8B5CF6). Circle diameter: 20% larger than the element. Add text labels positioned 1 inch from each circle with white text on semi-transparent dark grey background (85% opacity, Arial 13pt). Labels: 'USB-C Port', 'Power', 'Headphone Jack'. Connect each circle to its label with a thin white line (1px). Product remains pristine."

Example 2 - Callout Lines and Annotations:
"Mark each interface element with professional callout system. Draw thin white lines (2px) from each port at 45-degree angles to text boxes positioned in the right margin. Text boxes: white Arial 12pt on dark grey background (80% opacity) with 5px padding. Number each callout (1, 2, 3...). Maintain clean, technical manual aesthetic. Product unchanged, only overlay graphics added."

Example 3 - Subtle Glow Highlighting:
"Apply subtle glow effect to each port/button. Glow: soft white at 25% opacity with 8px blur radius. Add small floating labels nearby (white text, 11pt, no background). Labels positioned to not overlap with product. Minimal, clean approach that draws attention without cluttering. Product details remain sharp and unaltered."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Use method 1 (colored circles) as most versatile
- Choose contrasting colors that are visible against product
- Position labels to avoid obscuring product features
- Professional technical documentation style
- Clear, readable text (minimum 12pt)

REQUIREMENTS:
- Product 100% unchanged beneath overlays
- Highlights don't obscure important details
- Text is crisp and readable
- Professional, clean design
- All elements properly aligned

Generate the instruction.
"""
    },


    11: {
        "id": 11,
        "name": "Component Detailing & Connection Close-up",
        "category": "Plumbing, HVAC, Tools, Industrial",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Precision Technical Component Close-Up with Dimensional Accuracy

GOAL: Create a magnified view of technical components (valves, threads, couplings, connectors) that maintains EXACT proportional accuracy from the original image.

CRITICAL ACCURACY REQUIREMENT:
This is a TECHNICAL documentation shot. Proportions, dimensions, and spacing must be PRECISELY maintained from the source image. Users rely on these close-ups to understand exact component specifications, thread pitch, connection types, and fitment details.

DIMENSIONAL PRESERVATION MANDATE:
When zooming on threads, valves, or connections, you must:
- Count and preserve the EXACT number of visible thread grooves in the original image
- Maintain EXACT thread pitch (spacing between grooves) - measure and preserve ratio
- Preserve EXACT length-to-diameter ratios of threaded sections
- Maintain EXACT proportions between connected components (if connector is 1/3 the length of valve body in original, it stays 1/3 in close-up)
- Keep EXACT angular relationships (if fitting is at 90° angle, keep it at 90°)
- Preserve EXACT surface details (number of flats on hex nut, groove count, etc.)

MEASUREMENT ANALYSIS PROCESS:

Before generating the close-up, the LLM must analyze the original image:

1. IDENTIFY the target component clearly
2. COUNT visible details:
   - Number of thread grooves visible
   - Number of turns in a coil/spring
   - Number of flats on hex fittings
   - Number of sealing ridges/o-rings
   - Number of mounting holes/bolts

3. MEASURE proportional relationships:
   - Thread pitch: If 5 grooves span 10mm, each groove is 2mm apart → preserve this 2mm spacing in close-up
   - Length ratios: If threaded section is 1/4 of total component length → keep it 1/4
   - Diameter ratios: If connector diameter is 1/2 of valve body diameter → keep it 1/2
   - Depth ratios: If thread depth is 1/10 of thread diameter → maintain this ratio

4. NOTE surface characteristics:
   - Thread profile (V-thread, square thread, rounded)
   - Surface finish (smooth, knurled, brushed, rough-cast)
   - Material transitions (metal-to-rubber, brass-to-steel)
   - Wear patterns or machining marks

5. VERIFY scale consistency:
   - If original shows 8 threads in a 1-inch section, close-up must show same thread density
   - If gasket thickness is 1/20 of pipe diameter, maintain this ratio
   - If valve handle is 3x the width of the valve stem, keep this proportion

COMPONENT SELECTION PRIORITY:

If user doesn't specify which component to zoom on, analyze the product and select based on:

Priority 1 - Connection Interfaces:
- Threaded connections (most technical detail, shows fitment compatibility)
- Quick-connect fittings (shows mechanism clearly)
- Flanged connections (shows bolt pattern, gasket seating)
- Compression fittings (shows ferrule, nut, and pipe relationship)

Priority 2 - Precision Components:
- Valve seats and sealing surfaces
- Adjustment mechanisms (set screws, calibration points)
- Bearing surfaces or rotating interfaces
- Pressure relief mechanisms

Priority 3 - Quality Indicators:
- Machining quality on critical surfaces
- Thread quality and precision
- Material specifications (alloy markings, ratings)
- Manufacturing tolerances visible at component gaps

EXAMPLE APPROACHES:

Example 1 - Pipe Thread Close-up (NPT Threading):
"Target component: Male threaded end of pipe fitting visible on right side of product image.

DIMENSIONAL ANALYSIS of original image:
- Threaded section total length: Approximately 1.5 inches (measure against product for reference)
- Thread count visible: 11 complete thread grooves visible in original image
- Thread pitch calculation: 11 threads in 1.5 inches = 7.3 threads per inch (approximately 3/4" NPT standard)
- Thread depth: Grooves are approximately 1/15th of the outer diameter depth
- Taper: Threads show slight taper (0.75° per side for NPT) - wider at base, narrower at tip
- Transition point: Threads end and smooth pipe begins at a sharp shoulder, located 1.5" from pipe end
- Thread profile: 60-degree V-thread profile with flattened peaks and valleys (NPT standard)

CLOSE-UP COMPOSITION:
Zoom to 400% magnification, centered on the middle section of the threaded area.

Frame composition: 
- Threaded section fills 75% of frame width
- Show 8-9 complete thread grooves in the close-up view (proportionally correct for 400% zoom of 11-groove section)
- Include the thread-to-smooth pipe transition at the edge of frame for context (shows where threads end)

PROPORTIONAL ACCURACY in generated image:
- Thread spacing: 11 grooves in the full threaded section → if showing 60% of threaded section in close-up, display 6-7 grooves with IDENTICAL spacing ratio
- Thread pitch: Maintain 7.3 threads per inch density - grooves should appear evenly spaced at 0.137 inch intervals
- Thread depth: Groove depth remains 1/15th of outer diameter (if pipe shows as 30mm wide in close-up, grooves are 2mm deep)
- Thread profile: Maintain 60° angle, flattened peaks (not sharp V), consistent across all visible threads
- Taper: Show gradual diameter decrease from left to right (base to tip) - 1.5° total taper angle preserved
- Surface finish: Original shows brushed/machined finish - preserve the same directional machining marks running along thread length

LIGHTING for technical clarity:
Use 45-degree side lighting from upper-right to create shadows in thread valleys, making groove depth and profile clearly visible. Shadows in valleys should be 40% darker than peaks, clearly defining thread geometry.

Focus: Razor-sharp focus on threads, slight blur (8px) on background. No focus fall-off across threads - entire threaded section equally sharp.

Result: Technical documentation-quality image where a plumber/technician could verify thread type (NPT), estimate size (3/4"), and confirm compatibility - all proportions accurate to original."

Example 2 - Valve Seat and Washer Detail:
"Target component: Internal valve mechanism visible through partially opened valve assembly.

DIMENSIONAL ANALYSIS of original image:
- Valve seat diameter: Approximately 18mm (circular brass seat visible)
- Washer/gasket thickness: 2mm (measured as 1/9th of seat diameter)
- Washer outer diameter: 16mm (slightly smaller than seat, 8/9th ratio)
- Stem diameter passing through: 6mm (1/3 of seat diameter)
- Seat depth: 4mm deep recess (2/9th of diameter)
- Number of sealing ridges on washer: 2 concentric ridges visible

CLOSE-UP COMPOSITION:
Zoom to 500% magnification, centered on valve seat and washer interface.

Frame composition:
- Valve seat fills 60% of frame
- Show complete circular seat and washer
- Include portion of valve stem (above) and valve body (below) for spatial context - 20% of frame each

PROPORTIONAL ACCURACY in generated image:
- Seat diameter to washer diameter: Maintain 18mm:16mm ratio (9:8 ratio)
- Washer thickness: Maintain 2mm (1/9th of seat diameter) - if seat appears as 90mm in close-up, washer is 10mm thick
- Stem to seat ratio: Stem diameter is 1/3 of seat diameter - preserve this exactly
- Seat depth: 4mm recess (2/9th of diameter) - shows clear shadow/depth in close-up
- Sealing ridges: Show EXACTLY 2 concentric ridges on washer (not 1, not 3, exactly 2 as in original)
- Ridge height: Each ridge protrudes 0.5mm (1/4 of total washer thickness) - visible as raised circular lines

Material accuracy:
- Brass seat: Maintain golden brass color, smooth machined surface with circular machining marks
- Rubber washer: Black EPDM rubber, slightly textured surface, soft appearance
- Valve stem: Chrome-plated brass, highly reflective

LIGHTING for material definition:
Top-down lighting to show seat depth clearly. Add slight shadow in seat recess (30% darker than seat surface). Highlight reflection on brass seat (bright ring at edge where light catches machined surface). Rubber washer appears matte with no reflections.

Focus: Sharp focus on washer and seat contact area. Slight blur (5px) on valve stem above and valve body below.

Result: Proportionally accurate view where the exact washer size, thickness, seat diameter, and component relationships are preserved from original - useful for parts identification and replacement."

Example 3 - Coupling and Thread Engagement:
"Target component: Compression coupling connecting two pipe sections, visible in center of product.

DIMENSIONAL ANALYSIS of original image:
- Coupling nut length: 25mm (hexagonal nut portion)
- Threaded engagement length: 15mm (how far nut screws onto body)
- Ferrule (compression ring) position: Located 8mm from nut face
- Ferrule thickness: 3mm
- Pipe outer diameter: 12mm
- Thread count on coupling: 18 visible threads on the exterior male threads
- Hex nut: 6 flats, each flat is 8mm wide

CLOSE-UP COMPOSITION:
Zoom to 350% magnification, showing the coupling nut, ferrule, and pipe connection point.

Frame composition:
- Coupling nut (hexagonal portion) fills left 40% of frame
- Ferrule and pipe connection fills center 30%
- Pipe continuation fills right 30%
- Shows complete coupling assembly from nut face to 10mm past ferrule

PROPORTIONAL ACCURACY in generated image:
- Nut length to threaded length ratio: 25mm:15mm (5:3 ratio) - nut is 1.67x the threaded section length - maintain exactly
- Ferrule position: Located 8mm from nut face, which is 8/25 = 32% of nut length from face - preserve this position exactly
- Ferrule thickness to pipe diameter: 3mm:12mm (1:4 ratio) - ferrule is 1/4 of pipe diameter - maintain
- Thread pitch: 18 threads in 15mm = 1.2 threads per mm - if showing full threaded section, display 18 threads with equal spacing
- Thread engagement: Show that 15mm of threads are engaged (portion of threads hidden inside nut) - visible threads end where nut begins
- Hex nut proportions: Each of 6 flats is 8mm wide, nut is 25mm long - maintain 8:25 width-to-length ratio (nearly 1:3)

Assembly detail accuracy:
- Show ferrule compressed slightly against pipe (making conical seal contact)
- Pipe enters nut opening concentrically (pipe centered in nut bore)
- Gap between nut face and ferrule: Exactly 8mm (shows compression adjustment travel)

Material and surface details:
- Hex nut: Nickel-plated brass, 6 distinct flats with slight radius at edges (not sharp corners)
- Ferrule: Brass compression ring with beveled edge facing nut (45° bevel angle)
- Pipe: Copper with slight patina, smooth surface
- Threads: Machine-cut threads with consistent 60° profile

LIGHTING for assembly clarity:
Side lighting at 30° angle from left to create definition between nut flats and to cast shadow in the gap between nut and ferrule. Shadow in gap should be 50% darker, clearly showing the 8mm spacing.

Focus: Sharp focus across entire coupling assembly. Very slight blur (3px) on pipe sections extending beyond coupling area.

Result: Technically accurate view maintaining all dimensional relationships - a technician could verify ferrule position, thread engagement depth, and confirm proper assembly - all proportions match original exactly."

Example 4 - Quick-Connect Fitting Detail:
"Target component: Push-to-connect quick fitting on air line, visible on lower-left of product.

DIMENSIONAL ANALYSIS of original image:
- Fitting body outer diameter: 20mm
- Tube insertion depth: 12mm (visible mark where tube enters fitting)
- Release collar width: 6mm
- Release collar outer diameter: 24mm (1.2x body diameter)
- Number of visible o-ring grooves: 2 grooves on fitting body
- O-ring groove spacing: 4mm apart (center to center)
- Tube outer diameter: 8mm (2/5 of fitting body diameter)

CLOSE-UP COMPOSITION:
Zoom to 400% magnification centered on the tube insertion point and release collar.

Frame composition:
- Fitting body fills 50% of frame (center-left)
- Tube extends into right 30% of frame
- Release collar occupies center focus
- Show 12mm of tube insertion plus 15mm of fitting body and 10mm of external tube

PROPORTIONAL ACCURACY in generated image:
- Fitting to tube diameter: 20mm:8mm (5:2 ratio) - fitting is 2.5x tube diameter - maintain exactly
- Release collar to body diameter: 24mm:20mm (6:5 ratio) - collar is 1.2x body - maintain exactly
- Collar width to body diameter: 6mm:20mm (3:10 ratio) - collar is 3/10 of body diameter - preserve
- Tube insertion depth: 12mm visible, which is 3/5 of fitting body diameter (12/20) - maintain this ratio precisely
- O-ring groove spacing: 4mm apart, which is 1/5 of body diameter - if body shows as 100mm in close-up, grooves are 20mm apart
- O-ring count: EXACTLY 2 grooves visible (not 1, not 3), positioned 4mm apart measured center-to-center

Mechanical detail accuracy:
- Show collet teeth inside release collar (8 small teeth visible when looking at collar edge, each tooth approximately 1mm wide)
- O-rings: Seated in grooves, showing slight protrusion (0.5mm above groove surface)
- Tube insertion mark: Visible line where tube surface shows slight compression marking from o-ring contact

Material details:
- Fitting body: Nickel-plated brass, semi-reflective
- Release collar: Blue anodized aluminum, matte finish
- Tube: Clear polyurethane, semi-transparent showing slight internal refraction
- O-rings: Black nitrile rubber, visible in grooves as dark bands

LIGHTING for mechanism visibility:
Front-right lighting at 40° angle to illuminate internal collet teeth when looking into release collar. Add slight internal shadow showing collar depth. O-rings in grooves show shadow on trailing edge (groove depth appears as 1mm shadow).

Focus: Sharp focus on release collar and tube insertion point. Slight blur (6px) on tube extension beyond fitting and fitting body behind collar.

Result: Dimensionally accurate close-up showing exact tube size compatibility, insertion depth, o-ring positions, and fitting proportions - matches original image precisely, useful for verifying fitting size and tube compatibility."

Example 5 - Gear Teeth and Shaft Coupling:
"Target component: Gear teeth and keyway on drive shaft, visible on right side mechanism.

DIMENSIONAL ANALYSIS of original image:
- Gear outside diameter: 40mm
- Number of teeth: 24 teeth visible around circumference
- Tooth height: 3mm (from base circle to tip)
- Tooth width at base: 4mm
- Shaft diameter: 16mm (2/5 of gear diameter)
- Keyway width: 4mm (1/4 of shaft diameter)
- Keyway depth: 2mm (1/8 of shaft diameter)
- Tooth spacing (pitch): 360°/24 = 15° between teeth centers

CLOSE-UP COMPOSITION:
Zoom to 450% magnification showing 6-7 gear teeth and portion of shaft with keyway.

Frame composition:
- Gear teeth occupy top 60% of frame showing arc of 6 teeth
- Shaft with keyway occupies bottom 40%
- Transition from gear to shaft clearly visible

PROPORTIONAL ACCURACY in generated image:
- Tooth count in view: Show 6 complete teeth spanning approximately 90° of arc (6 × 15° = 90°)
- Tooth height to gear diameter: 3mm:40mm (3:40 ratio) - teeth are 7.5% of gear diameter - maintain exactly
- Tooth pitch: 15° spacing between tooth centers - if showing 6 teeth, they span exactly 90° of arc, evenly distributed
- Tooth width to height: 4mm:3mm (4:3 ratio) - teeth are slightly wider than tall at base - preserve ratio
- Shaft to gear diameter: 16mm:40mm (2:5 ratio) - shaft is 40% of gear diameter - maintain precisely
- Keyway width to shaft diameter: 4mm:16mm (1:4 ratio) - keyway is 1/4 shaft diameter - preserve exactly
- Keyway depth to shaft diameter: 2mm:16mm (1:8 ratio) - maintain this exact depth proportion

Tooth profile accuracy:
- Involute gear tooth profile: Curved flanks with specific geometry
- Tooth tip: Flat land approximately 1mm wide (1/3 of tooth height)
- Tooth root: Filleted radius approximately 0.5mm (prevents stress concentration)
- Each tooth IDENTICAL in shape and size (precision machining)

Keyway detail accuracy:
- Parallel-sided slot running along shaft length
- Sharp corners at 90° (machined, not rounded)
- Depth creates shadow showing 2mm recess (1/8 of shaft diameter as measured)
- Width exactly 4mm (1/4 of 16mm shaft diameter)

Material and manufacturing marks:
- Gear: Hardened steel, visible heat-treat discoloration (slight blue tint)
- Shaft: Bright steel, machined surface with circumferential tooling marks
- Keyway: Broached finish (parallel marks along keyway length)

LIGHTING for tooth geometry:
Side lighting from upper-left at 50° angle to create shadows on tooth flanks and in keyway. Shadow on trailing flank of each tooth shows tooth depth and involute profile. Shadow in keyway shows 2mm depth clearly (shadow is 60% darker than shaft surface).

Focus: Razor-sharp focus on all 6 visible teeth and keyway. Very slight blur (4px) on shaft and gear extending beyond main focus area.

Result: Precision mechanical view where tooth count, pitch, profile, shaft dimensions, and keyway specifications are all proportionally accurate to original - suitable for engineering verification or parts matching."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Analyze component and select most technical/informative detail
- Use priority list above (connections > precision parts > quality indicators)
- Default to 350-450% magnification
- Ensure all countable elements (threads, teeth, grooves) are accurately preserved
- Maintain all proportional relationships precisely

TECHNICAL EXECUTION REQUIREMENTS:

Dimensional Accuracy Checklist:
- ✓ Count original: threads, grooves, flats, holes, ridges
- ✓ Measure original: ratios of lengths, diameters, thicknesses, spacing
- ✓ Preserve counts: Same number of elements in close-up (scaled appropriately)
- ✓ Preserve ratios: All dimensional relationships maintained exactly
- ✓ Verify scale: If original shows X threads per inch, close-up shows same density

Image Quality:
- Sharp focus on primary component (no blur on technical details)
- Adequate depth of field (all critical surfaces in focus)
- No distortion (threads appear straight if they are straight, curved if curved)
- No artifacts (no added/missing details from AI hallucination)

Lighting for Technical Clarity:
- Directional lighting to reveal depth (threads, grooves, recesses)
- Shadows define geometry (30-60° lighting angle ideal)
- Reflections controlled (no glare obscuring details)
- Material properties visible (metal vs rubber vs plastic clearly distinguished)

Composition:
- Component centered and prominently displayed
- Context provided (10-20% of frame shows surrounding area)
- Orientation logical (threads shown along length, not end-on unless specifically detailed)

Professional Standards:
- Technical documentation quality
- Could be used for parts identification
- Could be used for compatibility verification
- Could be used for quality inspection reference

NEVER DO:
- Change proportions "for better composition" (accuracy over aesthetics)
- Add or remove threads/grooves/teeth for visual balance
- Exaggerate thread depth or spacing for clarity
- Simplify complex geometry
- Alter component relationships (change spacing, angles, or size ratios)
- Show components that don't exist in original image
- Fabricate technical details not visible in source

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific prompt that creates a dimensionally-accurate technical close-up maintaining exact proportions from the original image.
"""
    },

    12: {
        "id": 12,
        "name": "Product Variant Simulation",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Product Variant Creation

GOAL: Create alternate versions (color, finish, pattern) maintaining product identity

EXAMPLE VARIATIONS:

Example 1 - Color Variant:
"Create a variant with the main housing changed to deep blue (Hex: #003366). Maintain exact product geometry, all panel lines, vents, and features. Preserve the glossy finish characteristics - same reflectivity level, same highlight positions. Keep all logos, text, and warning labels in their original colors. Secondary components (buttons, grips, wheels) remain unchanged. The blue should have the same saturation intensity as the original red. All shadows and lighting remain identical."

Example 2 - Finish Variant (Glossy to Matte):
"Transform the finish from glossy to matte while keeping the color (red). Reduce specular highlights to 15% of current intensity. Add subtle micro-texture suggesting matte powder coating. Decrease reflectivity - no environmental reflections. Maintain all product details, shapes, and features exactly. The matte finish should look like professionally applied coating, not dull or chalky. Color saturation may reduce by 10-15% to appear realistic for matte finish."

Example 3 - Pattern Addition:
"Add a carbon fiber texture pattern to the main panels while maintaining the base color. Pattern: fine diagonal weave, 0.5mm grid scale, subtle depth variation. Apply only to flat panel surfaces, keep curved areas solid. Maintain product's glossy finish - the carbon fiber should have realistic clear-coat appearance. All other parts (metal components, rubber grips) remain unchanged. Professional automotive-grade carbon fiber aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Create a complementary color variant
- Maintain all geometric features
- Keep finish type consistent unless specified
- Preserve branding elements
- Professional product photography quality

REQUIREMENTS:
- Product shape 100% preserved
- Variant looks like real production option
- Consistent lighting and shadows
- All functional elements unchanged
- Realistic material rendering

Generate the instruction.
"""
    },

    13: {
        "id": 13,
        "name": "In-Room / Contextual Render",
        "category": "Furniture, Kitchen & Bath, Tools",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: In-Room or Contextual Placement

GOAL: Place product in realistic interior space or contextual environment

EXAMPLE ROOM SETTINGS:

Example 1 - Living Room Context:
"Place this chair in a modern minimalist living room. Positioning: center-right of frame, 30% from right edge, angled 25 degrees to show both front and side. Room details: light grey walls (Hex: #E5E5E5), medium oak hardwood floor in herringbone pattern, white sofa visible in background left (70% blur), single floor lamp with warm glow in far left, large window on right wall with sheer white curtains (soft natural light). Ceiling height: 9 feet standard. Chair maintains sharp focus while room is at 10px Gaussian blur. Scale: chair seat 18 inches from floor (realistic proportion relative to room)."

Example 2 - Workshop/Garage Setting:
"Show this tool in a residential garage workshop. Placement: on workbench in foreground left, occupying 50% of frame. Environment: pegboard wall in background with tools (slightly out of focus), concrete floor visible below, overhead LED shop lighting (5000K cool white). Include hints of other tools on bench (wrench, clamp) blurred. Red toolbox visible in background right at 12px blur. Product in sharp focus with all details clear. Realistic garage lighting with slight shadows."

Example 3 - Office Desk Context:
"Position the product on a clean, modern office desk. Desk: white laminate surface, minimalist design. Product placement: right third of frame. Visible context items (all blurred 8px): laptop partially visible left, notebook, pen, coffee mug. Background: hints of office - monitor edge, shelf with books, plant (all 12px blur). Lighting: cool LED office lighting (4000K) from overhead, window light from left side. Product sharp, environment provides professional context."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Choose contextually appropriate room for product type
- Natural, professional lighting
- Product in sharp focus (environment 8-12px blur)
- Realistic scale and proportions
- Clean, aspirational aesthetic

REQUIREMENTS:
- Product 100% unchanged in appearance
- Environment enhances, doesn't distract
- Realistic spatial relationships
- Proper lighting that makes sense
- Professional interior photography style

Generate the instruction.
"""
    },

    14: {
        "id": 14,
        "name": "Packaging Visualization",
        "category": "All",
        "test_image_type": "product_generic",
        "instruction_template": """
OPERATION: Intelligent Retail Packaging Design & Visualization

GOAL: Analyze the product and create the most effective, commercially-appropriate retail packaging that maximizes shelf appeal and brand presence.

STRATEGIC PACKAGING DECISION FRAMEWORK:

The LLM must analyze the product and DECIDE the optimal packaging approach based on:

PRODUCT ANALYSIS CRITERIA:

1. SIZE CATEGORY:
   - Small (< 6 inches): Blister pack, window box, or hanging card
   - Medium (6-24 inches): Window box, full box with graphics, or display box
   - Large (24-48 inches): Full cardboard box with handles, product image graphics
   - Oversized (> 48 inches): Shipping-style box, industrial packaging, strapped/wrapped

2. VALUE/PRICE POINT (infer from product type):
   - Budget/Economy: Simple cardboard box, shrink wrap, basic graphics
   - Mid-range: Color box with window or product photo, professional branding
   - Premium/Luxury: High-end box materials, magnetic closure, embossing, elegant design
   - Professional/Industrial: Functional packaging, foam inserts, technical specs displayed

3. PRODUCT VISIBILITY BENEFIT:
   - High benefit (attractive product): Transparent window, blister pack, open display
   - Medium benefit: Partial window showing key feature, or high-quality product photo
   - Low benefit (complex/technical): Full box with detailed graphics, cutaway illustration

4. RETAIL CONTEXT:
   - Hanging display (peg hooks): Hanging card with header, blister pack, hook hole
   - Shelf display: Box that stands vertically, attractive front panel
   - Counter display: Compact box with 360° branding
   - Warehouse/online: Protective shipping box with minimal graphics

5. PRODUCT CATEGORY NORMS:
   - Electronics: Window boxes, premium materials, tech-focused graphics
   - Tools: Rugged boxes, clear windows showing tool, hang-able options
   - Beauty/Cosmetics: Elegant boxes, product visibility, luxury feel
   - Toys: Vibrant graphics, large windows, character branding
   - Industrial: Plain brown boxes, labels with specs, protective interior

PACKAGING TYPE DECISION TREE:

SMALL PRODUCTS (< 6 inches):

Choice A - Blister Pack with Hanging Card:
- When: Impulse buy items, tools, accessories, small electronics
- Design: Clear plastic blister showing full product, cardboard backing with branding
- Features: Euro-slot hang hole at top, product visible 100%, theft-deterrent

Choice B - Small Window Box:
- When: Premium small items, cosmetics, tech accessories
- Design: Rigid cardboard box with die-cut window, product visible from front
- Features: Magnetic or tuck-flap closure, elegant printing

Choice C - Full Graphic Box:
- When: Product is less visually interesting but brand is strong
- Design: Complete cardboard box with product photo/illustration
- Features: Lists features, shows product in use, professional photography

MEDIUM PRODUCTS (6-24 inches):

Choice A - Large Window Box:
- When: Product appearance is a selling point
- Design: Substantial cardboard box with large acetate/PET window (covers 40-60% of front)
- Features: Product centered in window, branding above/below, feature callouts on sides

Choice B - Photo Box (No Window):
- When: Product is bulky or complex, difficult to display well through window
- Design: High-quality product photography on front panel, lifestyle image on side
- Features: Premium printing, embossed logo, feature highlights, die-cut handle optional

Choice C - Display/Open Box:
- When: Premium presentation, demonstration units
- Design: Partial box showing top half of product, product can be touched
- Features: Retail counter placement, try-before-buy appeal

LARGE PRODUCTS (24-48 inches):

Choice A - Retail Box with Handle:
- When: Furniture, large appliances, assembled items
- Design: Full-color printed corrugated box, die-cut handle holes on top/sides
- Features: Large product image on front, dimensions/specs on side, assembly icons

Choice B - Shrink-Wrapped with Band:
- When: Product is attractive and sturdy (chairs, grills, etc.)
- Design: Clear shrink wrap with branded cardboard band/label around middle
- Features: Product fully visible, 360° view, minimal packaging waste

OVERSIZED/HEAVY PRODUCTS (> 48 inches):

Choice A - Industrial Shipping Box:
- When: Machinery, large appliances, heavy equipment
- Design: Brown corrugated cardboard, reinforced corners, strapping
- Features: Printed label with product photo, specs, handling icons (fragile, this-side-up)

Choice B - Crate/Pallet Packaging:
- When: Very heavy or valuable equipment
- Design: Wooden crate or banded pallet wrap
- Features: Stenciled markings, shipping labels, corner protectors

EXAMPLE PACKAGING DECISIONS:

Example 1 - Small Electronics (Bluetooth Earbuds):
"Product analysis:
- Size: 2 inches (small case)
- Category: Consumer electronics
- Price point: Mid-range ($50-100 inferred from design quality)
- Visibility benefit: High (sleek design, color options)
- Retail context: Counter display or shelf

PACKAGING DECISION: Premium window box with magnetic closure

Box design:
- Dimensions: 4" W × 5" H × 2" D (compact, premium feel)
- Material: Rigid cardboard (300gsm), matte black finish
- Window: Clear PET plastic window on front panel, shaped to product silhouette (oval cutout 2.5" × 3"), showing earbuds case centered
- Product position: Earbuds case sits in molded paper pulp insert, positioned to be visible through window, slightly tilted (15° angle) for dynamic look
- Closure: Magnetic flap closure (hidden magnets in flap and base for clean look)

Box graphics:
- Front: Minimal branding - small brand logo (0.5" height) top-center above window, product name below window in silver foil text
- Top panel: Brand name and product features (wireless, battery life, noise cancelling) in white text
- Back panel: Product specifications, feature icons, box contents list
- Side panels: Product colorway indicator (small color dot showing which color inside)

Interior:
- Molded paper pulp insert holding earbuds case securely
- Accessories (cable, tips) in separate compartment under main tray
- Quick start guide tucked into lid

Box positioning: Stands vertically on shelf, front window facing customer.

Color scheme: Matte black box, white text, silver accents, clear window - premium tech aesthetic."

Example 2 - Power Tool (Cordless Drill):
"Product analysis:
- Size: 10 inches long
- Category: Power tools
- Price point: Professional grade ($150+)
- Visibility benefit: High (customers want to see build quality)
- Retail context: Shelf or hanging pegboard

PACKAGING DECISION: Rugged window box with hang tab

Box design:
- Dimensions: 12" W × 14" H × 4.5" D
- Material: Heavy-duty corrugated cardboard (E-flute), glossy finish
- Window: Large rectangular clear plastic window (7" × 10"), positioned to show drill body and battery
- Product position: Drill suspended in vacuum-formed plastic tray, visible through window with handle facing right, battery attached
- Hang feature: Reinforced cardboard header with euro-slot hole (can hang or stand on shelf)

Box graphics:
- Front: Bold brand logo top-left (2" width), large product photo showing drill in action (background of main panel), window overlays this, key features in callout bubbles ("20V MAX", "500 in-lbs Torque")
- Header (above hang hole): Brand name + product model number
- Back panel: Detailed specs table, battery compatibility chart, what's included list
- Side panels: Product in use (person drilling), brand logo

Interior:
- Vacuum-formed clear plastic tray holding drill, battery, charger, and bit set
- Cardboard backing behind tray (prevents theft, can't remove items without opening)
- Instruction manual sleeved into lid

Box positioning: Can hang on pegboard via euro-slot OR stand vertically on shelf.

Color scheme: Brand colors (typically yellow/black for DeWalt, red for Milwaukee, green for Ryobi), high-contrast text, action photography."

Example 3 - Beauty Product (Luxury Facial Serum):
"Product analysis:
- Size: 1 oz bottle (3 inches tall)
- Category: Premium skincare
- Price point: Luxury ($80+)
- Visibility benefit: Medium (elegant bottle design, but ingredients/brand story also important)
- Retail context: Counter display, boutique shelf

PACKAGING DECISION: Luxury rigid box with partial window

Box design:
- Dimensions: 3" W × 4.5" H × 2" D
- Material: Rigid chipboard wrapped in premium textured paper (linen finish), white/cream color
- Window: Small die-cut circular window (1.5" diameter) on front, positioned to show just the top of bottle/cap (teaser view)
- Product position: Bottle sits in foam insert, nested securely, only top visible through window
- Closure: Sleeve-style box (outer sleeve slides up to reveal inner tray) OR magnetic closure lid

Box graphics:
- Front: Embossed/debossed brand logo (no ink, just texture), small window, minimal text ("Radiant Renewal Serum" in elegant serif font)
- Top: Brand name embossed
- Back: Ingredients list, usage instructions, brand story in small elegant typography
- Interior lid: Hidden message or brand manifesto printed inside lid (customer discovers when opening)

Interior:
- White or cream foam insert with precision-cut cavity for bottle
- Bottle sits upright, surrounded by protective foam
- Information card/leaflet tucked beside bottle (ingredients, sustainability story, usage tips)

Box positioning: Stands on counter or shelf, front facing out, invitation to pick up and open.

Color scheme: Minimalist - white/cream box, gold or silver foil accents, soft natural tones - luxury skincare aesthetic."

Example 4 - Furniture (Office Chair):
"Product analysis:
- Size: 24" W × 40" H (assembled)
- Category: Furniture
- Price point: Mid-range office furniture
- Visibility benefit: Low (bulky when packaged, better shown via photo)
- Retail context: Warehouse shelf, online fulfillment

PACKAGING DECISION: Full graphic box with handle

Box design:
- Dimensions: 26" W × 12" H × 24" D (flat-packed chair components inside)
- Material: Heavy corrugated cardboard (double-wall), brown kraft exterior
- No window: Full box with printed graphics
- Handle: Die-cut handles on both short sides (2" × 5" oval cutouts, reinforced with cardboard doubler)

Box graphics:
- Front panel: Large high-quality photo of assembled chair (lifestyle setting - home office), brand logo top-left corner (3" width), product name below logo
- Top panel: Assembly difficulty icon (showing "easy assembly"), estimated assembly time (15 min), tools required icon
- Side panels: Product dimensions diagram, weight capacity (250 lbs), feature callouts (adjustable height, lumbar support, 360° swivel)
- Back panel: Assembly instructions preview (3-step illustrated guide), customer service QR code, sustainability certifications

Interior:
- Components flat-packed: seat, back, base, wheels, hardware pack
- Each component wrapped in protective foam/cardboard
- Hardware in labeled plastic bag
- Assembly instructions booklet
- Allen key included

Box positioning: Stored flat on warehouse shelf, customer carries via handles.

Color scheme: Brown kraft box with full-color photo print (vibrant to stand out in warehouse aisle), brand colors in logos/accents."

Example 5 - Industrial Equipment (Air Compressor):
"Product analysis:
- Size: 20" W × 20" H × 10" D, 45 lbs
- Category: Professional tools/industrial
- Price point: Professional ($300+)
- Visibility benefit: Low (complex machinery, specs matter more than appearance)
- Retail context: Industrial supply store, contractor warehouse

PACKAGING DECISION: Heavy-duty shipping box with labeled graphics

Box design:
- Dimensions: 22" W × 22" H × 12" D
- Material: Heavy double-wall corrugated cardboard, reinforced corners
- No window: Fully enclosed protective packaging
- Handles: Rope handles on sides OR die-cut reinforced handles

Box graphics:
- Front panel: Product photo on white background (clean product shot showing compressor), large brand logo above photo, model number below in bold
- Top panel: Handling icons (heavy item, this side up, fragile)
- Side panels: Technical specifications table (PSI, CFM, tank size, HP, voltage), QR code linking to manual/video
- End panels: Brand logo, "Professional Series" badge
- All panels: Printed in 2-color (black + brand color on kraft brown) for cost efficiency

Interior:
- Compressor wrapped in foam corner protectors
- Accessories (hose, fittings, regulator) in separate cardboard partition box
- Manual and warranty card in plastic sleeve taped to inside lid
- Foam or cardboard padding around entire unit

Box positioning: Stacked on pallet or shelf, front panel facing out.

Handling features:
- Reinforced bottom with double-thick cardboard
- Edge protectors at all corners
- Shrink-wrap band around entire box (extra security for heavy item)

Color scheme: Kraft brown box, black and brand color printing (typically orange, red, or blue for industrial brands), high-contrast text for spec readability."

USER SPECIFICATIONS:
{user_details}

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific prompt that creates a appropriate packaging visualization for the product in the input image.
"""
    },

    15: {
        "id": 15,
        "name": "Texture Enhancement",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Surface Texture Enhancement

GOAL: Enhance and emphasize surface textures (metal, fabric, wood, plastic)

EXAMPLE ENHANCEMENTS:

Example 1 - Metal Texture:
"Enhance the brushed metal texture on all metallic surfaces. Increase micro-texture visibility by 40% - show directional grain lines (0.2mm width) more prominently. Add subtle anisotropic reflections that follow grain direction. Enhance the contrast between texture peaks (slightly brighter) and valleys (slightly darker) by 25%. Maintain overall color and finish. The enhancement should reveal machining marks and surface treatment detail without looking artificial. Professional product photography aesthetic."

Example 2 - Fabric Weave:
"Amplify the fabric weave texture to show individual thread crossings. Increase weave pattern visibility by 50% - make warp and weft threads distinct. Use subtle lighting to create micro-shadows in weave valleys. Enhance texture depth without changing fabric color or overall appearance. Show fabric nap direction through subtle shading. Maintain fabric's drape and form exactly. The result should look like professional macro textile photography."

Example 3 - Wood Grain Enhancement:
"Emphasize natural wood grain pattern. Increase grain line contrast by 35% - darker grain lines against lighter wood. Show subtle depth variations following growth rings. Enhance micro-texture of wood pores and surface. Maintain wood's natural color - just reveal more detail. Add subtle highlights on wood ridges from side lighting. Result should appear like high-resolution wood photography, not artificial or over-processed."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Enhance texture by 30-40%
- Maintain overall color
- Add micro-detail visibility
- Natural, not over-processed appearance
- Professional photography quality

REQUIREMENTS:
- Product shape and color preserved
- Texture enhancement looks natural
- No artificial patterns added
- Appropriate for material type
- Professional, subtle enhancement

Generate the instruction.
"""
    },

        16: {
        "id": 16,
        "name": "Ingredient / Feature Highlight Visualization",
        "category": "Beauty, Electronics, Tools, Industrial",
        "test_image_type": "beauty_bottle",
        "instruction_template": """
OPERATION: Premium Feature Highlight (Product-Focused)

GOAL: Create a high-end marketing image that highlights a key feature using only text and background modifications, ensuring the product remains the clear, unobstructed hero.

ABSOLUTE PRIMARY RULE:
**The product MUST remain 100% visible, pristine, and unobstructed.** No visual effects, glows, swirls, particles, or abstract elements should float in front of or around the product. The product is the hero of the shot.

INTELLIGENT FEATURE SELECTION (if user does not specify):
Analyze the product to identify a compelling feature to highlight.
- For Beauty: A hero ingredient (Vitamin C, Hyaluronic Acid).
- For Electronics: A key technology (AI Noise Cancellation, Quantum Dot Display).
- For Tools: A core benefit or material (Brushless Motor, Titanium-Coated).

CREATIVE APPROACHES (Non-Obstructive):

Approach A: Thematic Background with Clean Text
The background changes to thematically represent the feature, while the product stays pristine in the foreground. This creates a powerful visual story without touching the product itself.
- Example for "Cooling Technology": "Keep the product in the foreground, perfectly sharp and unchanged. Transform the background into a clean, minimalist surface of frosty, textured ice with subtle blue backlighting. Place the text 'VAPOR-CHAMBER COOLING' in a clean, open space in the bottom right."
- Example for "Rose Petal Ingredient": "Keep the cosmetic bottle in sharp focus. Replace the background with a soft-focus, artistic bed of pink rose petals, creating a beautiful, blurred texture behind the product. Place the text 'ROSEWATER INFUSED' in an elegant serif font in the top left corner."

Approach B: Minimalist Studio with Impactful Text
The background is a clean, professional studio setting (gradient, solid color, or textured surface). The typography is the main creative element.
- Example for "Brushless Motor": "Place the tool on a dark, textured concrete surface against a simple dark gray studio background. Use dramatic side-lighting to highlight the tool's form. Place the text 'BRUSHLESS MOTOR' in a bold, white, industrial sans-serif font in the lower third of the image. Below it, in a smaller font, add 'More Power. Longer Life.'"
- Example for "Feather-Light": "Position the product against a clean, white-to-light-gray gradient background. Use soft, even lighting to create a feeling of lightness. Place the text 'ULTRA-LIGHT FRAME' in a thin, elegant, gray font, positioned artfully in the negative space to the right of the product."

TEXT OVERLAY DESIGN & STYLE:

Font Hierarchy:
- Headline: A bold, impactful font for the feature name (e.g., "BRUSHLESS MOTOR").
- Sub-text (optional): A lighter, smaller font for a brief benefit statement (e.g., "More Power, Longer Life").
- Font choice must match the brand's personality (e.g., Serif for luxury, Sans-serif for tech).

Color & Contrast:
- Text color must have high contrast with its immediate background.
- For readability on any background, you can place the text within a subtle, semi-transparent dark or light shape.

Positioning:
- Place text in areas of negative space (e.g., top-left, bottom-right).
- **CRITICAL:** DO NOT place text directly over the product or obscure any part of it. The product and text should be two separate, balanced elements in the composition.

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Intelligently select a single, compelling feature to highlight based on the product image.
- Choose one of the non-obstructive creative approaches above.
- Generate a concise, powerful headline for the feature.

FINAL CHECKLIST (MANDATORY RULES):
- ✓ Is the product 100% visible and unobstructed?
- ✓ Are there NO floating particles, glows, swirls, or effects covering the product?
- ✓ Does the text overlay have its own clean space?
- ✓ Does the final image look like a professional, high-end advertisement?
- ✓ Is the composition balanced and aesthetically pleasing?

Generate a hyper-specific instruction for Nano Banana to create a creative feature highlight where the product is the hero.
"""
    },

    17: {
        "id": 17,
        "name": "Lighting & Exposure Correction",
        "category": "All",
        "test_image_type": "product_snowblower",
        "instruction_template": """
OPERATION: Lighting and Exposure Optimization

GOAL: Correct brightness, contrast, highlights, and shadows for optimal exposure

EXAMPLE CORRECTIONS:

Example 1 - Underexposed Recovery:
"Increase overall brightness by 20% to achieve proper exposure. Lift shadow detail by 30% to reveal features in dark areas without losing depth. Reduce highlight clipping by recovering 25% detail in bright areas (chrome, reflective surfaces). Boost midtone contrast by 15% to add punch. Maintain color accuracy throughout - no color shifts. The result should look naturally well-lit, not artificially brightened. Professional product photography exposure."

Example 2 - Overexposed Correction:
"Reduce overall exposure by 18% to bring into proper range. Recover blown highlights by 35% - restore detail in overexposed areas (white surfaces, metallic parts). Maintain shadow depth - don't let shadows become muddy. Adjust contrast to compensate: increase by 12% for clarity. Keep whites truly white, not grey. Product should appear correctly exposed as if photographed with proper lighting."

Example 3 - Contrast Enhancement:
"Optimize contrast for product clarity. Increase overall contrast by 20%. Stretch tonal range - deepen shadows by 15%, brighten highlights by 10%. Ensure separation between product and background. Add micro-contrast (clarity) by 25% to enhance texture visibility. Maintain natural appearance - avoid harsh, artificial look. Result: crisp, professional product image with excellent tonal separation."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Analyze image and correct to neutral, proper exposure
- Recover highlight/shadow detail as needed
- Optimize contrast for product clarity
- Maintain color accuracy
- Professional photography standards

REQUIREMENTS:
- Natural-looking result
- No detail loss
- Colors remain accurate
- Proper tonal balance
- Product details clearly visible

Generate the instruction.
"""
    },

    18: {
        "id": 18,
        "name": "White Balance Adjustment",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: White Balance and Color Temperature Correction

GOAL: Correct color temperature to achieve accurate, neutral colors

EXAMPLE CORRECTIONS:

Example 1 - Warm Cast Removal:
"Correct warm yellow/orange color cast. Shift color temperature from approximately 3200K to neutral 5500K (daylight). Reduce yellow in shadows and midtones. Adjust tint by -5 points toward magenta to neutralize green undertone. Use the grey/white components as neutral reference points. Ensure the product red maintains true hue (not orange-red). Black areas should be neutral, not warm brown. Result: accurate daylight-balanced colors."

Example 2 - Cool Cast Correction:
"Remove cool blue color cast. Warm the image from approximately 7000K to neutral 5500K. Add warmth to counteract blue tint, especially in highlights and white areas. Adjust tint by +3 points toward green to balance magenta cast. Reference neutral grey elements for accuracy. Product colors should appear as they would under natural daylight - no blue contamination in whites or greys."

Example 3 - Mixed Lighting Fix:
"Correct mixed lighting conditions (tungsten + daylight). Globally adjust to 5500K neutral. Selectively correct areas with different color casts if needed. Ensure all whites/greys are neutral across the entire image. Product brand colors (reds, blues) should match standard color references. Remove any color shifts in shadows or highlights. Professional color-accurate result."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Correct to neutral daylight (5500K)
- Use grey/white elements as reference
- Remove all color casts
- Maintain product's true colors
- Professional color accuracy

REQUIREMENTS:
- Neutral, accurate white balance
- No color contamination in neutrals
- Product colors true to life
- Consistent across entire image
- Professional color correction standards

Generate the instruction.
"""
    },

    19: {
        "id": 19,
        "name": "Color Correction (Hue/Saturation/Vibrance)",
        "category": "All",
        "test_image_type": "product_snowblower",
        "instruction_template": """
OPERATION: Precise Color Matching and Correction

GOAL: Adjust colors to accurately match physical product

EXAMPLE CORRECTIONS:

Example 1 - Brand Color Matching:
"Correct the red housing to match exact brand color (Toro Red - Hex: #DA291C). Shift red hue by +3 degrees toward orange-red. Increase red saturation by 12% for brand vibrancy. Apply selective color correction - only affect red channel, keep grey/black components unchanged. Maintain realistic appearance - the red should look like automotive-grade paint, not artificial. Chrome and metallic parts preserve their neutral colors exactly."

Example 2 - Multi-Color Balance:
"Balance all product colors for accuracy. Red areas: shift hue +2°, increase saturation 10%. Black components: ensure neutral (no color tint), deepen to true black. Grey metal: remove any color cast, maintain metallic sheen. Rubber grips: slight desaturation by 5% for realistic matte appearance. Overall vibrance increase by 8% for product appeal while maintaining natural look."

Example 3 - Saturation Recovery:
"Restore color saturation to appear as real product. Increase overall vibrance by 15% (affects muted colors more than saturated). Protect already-saturated areas from oversaturation. Boost product primary color (red) saturation by 18%. Maintain neutral colors (whites, greys, blacks) at current saturation. Result: vibrant, appealing colors that match physical product without looking artificial or oversaturated."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Match colors to what appears most natural for product type
- Increase vibrance by 10-15% for appeal
- Maintain neutral colors accurately
- Avoid oversaturation
- Professional product photography color

REQUIREMENTS:
- Colors match real product
- Natural appearance maintained
- No color bleed or contamination
- Appropriate saturation levels
- Professional color grading

Generate the instruction.
"""
    },
    20: {
    "id": 20,
    "name": "Background Removal / Isolation",
    "category": "All",
    "test_image_type": "product_tool",
    "instruction_template": """You are an expert in AI image editing, specifically using a model that understands natural language commands to perform edits. Your task is to generate a detailed, hyper-specific prompt for an AI image editing model, 'nano banana', to achieve a desired image manipulation. The generated prompt should be clear, concise, and provide all the necessary information for the AI to produce a high-quality result.

    **Analysis of the Request:**

    1.  **Identify the Core Objective:** What is the primary goal of the user's request? (e.g., remove the background, change the background, add an object, alter a specific detail, etc.)
    2.  **Identify the Subject:** What is the main subject of the image that needs to be preserved or modified?
    3.  **Identify the Action:** What specific action needs to be performed on the subject or the background?

    **Prompt Generation Guidelines:**

    *   **Be Specific and Descriptive:** Use vivid and precise language. Instead of "make the background nice," use "change the background to a soft-focus, professional photography studio with a neutral grey backdrop."
    *   **Focus on a Single, Clear Instruction:** While nano banana can handle multi-step instructions, for the best results, generate a prompt that focuses on a single, coherent instruction.
    *   **Preserve Key Elements:** Explicitly state what should be preserved in the image, especially the main subject. Mention details like lighting, shadows, and reflections to ensure a realistic result.
    *   **Use Negative Prompts:** If necessary, specify what should *not* be in the final image. For example, "no extra objects," "no text," "no watermarks."
    *   **Consider the Style:** If the user's request implies a certain style (e.g., "make it look more professional," "give it a vintage feel"), translate that into concrete visual descriptions. For example, for a "vintage feel," you might include "apply a warm, sepia-toned filter and add a subtle film grain effect."
    *   **Structure the Prompt Logically:** Start with the main action, then describe the subject, and finally, add details about the desired outcome.

    **Example Prompt Structure:**

    "[Action] the [Subject]. The [Subject] should be [Description of the subject's desired state]. The background should be [Description of the new background or state]. Ensure that [Details to preserve or enhance]. Avoid [Negative prompts]."

    **Your Task:**

    Based on the user's request for image editing, generate a prompt that follows these guidelines to be used with the 'nano banana' AI image editing model. The prompt should be a single block of text.

    USER SPECIFICATIONS:
    {user_details}

    **Generated Prompt for nano banana:**

    [The LLM would generate the detailed, hyper-specific prompt here]"""
    },

    21: {
        "id": 21,
        "name": "Shadow & Reflection Generation",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Add Realistic Shadows and Reflections

GOAL: Generate natural-looking shadows and/or reflections beneath product

EXAMPLE APPROACHES:

Example 1 - Soft Drop Shadow:
"Add realistic soft drop shadow beneath the product. Shadow characteristics: color RGB(0,0,0) at 40% opacity, 20px Gaussian blur, 6px vertical offset downward, 2px horizontal offset right (suggesting light from top-left). Shadow shape follows product's base contours - wider under wheels/feet, narrower under raised portions. Shadow darkest directly under product (50% opacity), fading to transparent at edges (10% opacity at 3-inch distance). Natural, grounding effect."

Example 2 - Contact Shadow with Reflection:
"Create contact shadow plus subtle reflection on glossy surface. Shadow: dark grey (RGB 50,50,50) at 35% opacity, 15px blur, starting at product base. Reflection: 18% opacity mirror of product's underside, 8px vertical Gaussian blur to suggest glossy floor, fading to transparency within 6 inches. Reflection shows product bottom (wheels, base) faintly. Combined effect suggests product on polished surface with studio lighting."

Example 3 - Ambient Occlusion Shadow:
"Generate soft ambient occlusion shadow suggesting indoor diffused lighting. Shadow: very soft grey (RGB 80,80,80) at 30% opacity, 25px blur, no offset (centered under product). Shadow size: 90% of product footprint. Edges fade smoothly to transparent. No hard edges - completely soft and natural. Subtle grounding effect without strong directionality. Professional product photography aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Soft drop shadow approach (Example 1)
- 40% opacity, 20px blur
- Slight offset suggesting top-left lighting
- Natural, not overdone
- Professional and subtle

REQUIREMENTS:
- Shadow shape matches product base
- Opacity and blur look natural
- Doesn't obscure product details
- Professional photography quality
- Grounding effect without being dominant

Generate the instruction.
"""
    },

    22: {
        "id": 22,
        "name": "Background Replacement",
        "category": "All",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: Replace Background with New Scene

GOAL: Replace existing background while keeping product unchanged

EXAMPLE REPLACEMENTS:

Example 1 - Studio to Lifestyle:
"Replace plain background with modern interior setting. New background: light grey walls (Hex: #D3D3D3), medium oak hardwood floor in diagonal pattern, blurred window with sheer curtains on left (12px blur), white trim visible. Maintain product position and lighting - shadows should match new environment. Apply 10px Gaussian blur to entire background to keep focus on product. Ensure product edges are clean with 0.5px feathering. Background should complement product without competing for attention."

Example 2 - Outdoor Context:
"Replace background with outdoor patio setting. New background: wooden deck boards (horizontal orientation), potted plants softly blurred in background (15px blur), hints of outdoor furniture far background. Sky visible above with soft clouds (heavily blurred). Natural outdoor lighting consistent with product's existing shadows. Background 70% desaturated to keep focus on product. Product maintains sharp focus and all details."

Example 3 - Gradient Background:
"Replace with professional gradient background. Gradient: top RGB(240,240,245) smoothly transitioning to bottom RGB(255,255,255). Subtle radial gradient behind product (slightly lighter in center). Clean, simple, professional. Product cutout precise with 1px feathering. Add appropriate shadow (soft grey, 35% opacity, 18px blur) on new background. Studio photography aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Clean gradient or solid color background
- Professional and simple
- Complements product colors
- Appropriate shadow added
- Product focus maintained

REQUIREMENTS:
- Product 100% unchanged
- Background blur maintains focus on product
- Clean edges on product cutout
- Lighting/shadows make sense together
- Professional composition

Generate the instruction.
"""
    },

    23: {
        "id": 23,
        "name": "Depth & Shadow Mapping",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Enhanced Depth and 3D Shadow Mapping

GOAL: Add depth cues and shadow mapping for realistic 3D appearance

EXAMPLE APPROACHES:

Example 1 - Multi-Layer Shadows:
"Create layered shadow system for depth. Layer 1 (Contact shadow): Dark grey (RGB 40,40,40) at 50% opacity, 8px blur, directly under product. Layer 2 (Ambient shadow): Medium grey (RGB 100,100,100) at 30% opacity, 25px blur, extends 8 inches from product base. Layer 3 (Vignette): Subtle darkening of floor corners (15% opacity) to focus attention. Shadow gradient: darkest nearest product, fading smoothly to transparent. Creates strong sense of grounding and depth."

Example 2 - Atmospheric Perspective:
"Enhance depth through atmospheric effects. Floor: subtle gradient from darker (foreground - RGB 245,245,245) to lighter (background - RGB 255,255,255). Very subtle desaturation of background by 8%. Add progressive shadow: strongest under product (45% opacity), gradually lighter extending backward (fading to 5% at 12 inches). Micro-vignette darkening image edges by 10%. Product appears to occupy real space."

Example 3 - Depth of Field Simulation:
"Simulate depth through selective focus effects. Product: maintain sharp focus. Floor immediately around product (6-inch radius): sharp. Floor beyond 12 inches: progressive blur starting at 3px, increasing to 15px at edges. Shadows: sharp near product, softer with distance. Subtle depth cues without strong blur. Professional large-format camera aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Multi-layer shadow approach (Example 1)
- Creates strong depth perception
- Natural shadow falloff
- Subtle, professional effect
- Product clearly grounded in space

REQUIREMENTS:
- Natural depth cues
- Shadows follow physics principles
- Product remains sharp and clear
- Professional photography aesthetic
- Realistic 3D appearance

Generate the instruction.
"""
    },

    24: {
        "id": 24,
        "name": "Environmental Lighting Simulation",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Simulate Different Lighting Conditions

GOAL: Re-light product to match specific environment (daylight, indoor, studio, etc.)

EXAMPLE LIGHTING SCENARIOS:

Example 1 - Soft Window Daylight:
"Re-light with soft natural window light simulation. Main light (key): from left at 45-degree angle, soft and diffused (5500K color temperature). Characteristics: soft shadows (30% opacity, 20px blur) falling to the right, gentle highlight on left-facing surfaces. Fill light: subtle from right at 25% intensity to lift shadows. No harsh edges - completely soft studio daylight. Product colors accurate under daylight. Shadows show direction but remain soft and natural."

Example 2 - Studio Three-Point Lighting:
"Apply professional studio lighting setup. Key light: top-left at 45°, bright (80% intensity), creates defined shadows. Fill light: camera-right at 30% intensity, softens shadows without eliminating them. Rim light: behind-right at 40%, adds edge highlights on product contours. Shadows: moderate opacity (40%), medium softness (15px blur). High-end product photography lighting. Specular highlights on reflective surfaces aligned with light positions."

Example 3 - Warm Indoor Lighting:
"Simulate warm indoor lighting (3000K tungsten). Overall warm color shift - add 10% yellow/orange tint. Softer contrast than daylight (reduce by 15%). Lighting from above-front, creating gentle downward shadows (35% opacity, 18px blur). Slightly enhance warm tones in product's lighter areas. Maintain shadow depth while keeping warm, inviting atmosphere. Cozy interior lighting feel."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Soft natural daylight (Example 1)
- 5500K neutral color temperature
- Soft shadows, balanced lighting
- Professional product photography
- Natural and appealing

REQUIREMENTS:
- Lighting appears natural for chosen type
- Shadows match light direction
- Color temperature consistent throughout
- Product well-lit and clear
- Professional photography quality

Generate the instruction.
"""
    },

    25: {
        "id": 25,
        "name": "HDR Simulation",
        "category": "Electronics, Jewelry, Tools",
        "test_image_type": "electronics_laptop",
        "instruction_template": """
OPERATION: HDR (High Dynamic Range) Effect

GOAL: Expand tonal range showing detail in both highlights and shadows

EXAMPLE HDR APPROACHES:

Example 1 - Balanced HDR:
"Apply balanced HDR processing. Recover highlight detail: reduce brightest areas by 40% to reveal texture in chrome, reflective surfaces. Lift shadow detail: increase darkest areas by 35% to show features in recesses without losing depth. Boost local contrast (clarity) by 25% to enhance texture and edges. Avoid halos - use 1px edge feathering in transitions. Maintain natural appearance - not over-processed HDR look. Result: rich detail throughout tonal range while keeping realistic appearance."

Example 2 - Detail Enhancement HDR:
"Apply HDR for maximum detail visibility. Highlight recovery: 45% reduction in bright areas. Shadow lift: 40% increase in dark areas. Local contrast boost: 30% increase (clarity/structure). Micro-contrast enhancement on textures. Edge sharpening: subtle 15% increase. Careful halo prevention - blend zones smoothly. The goal: see detail in every area (bright metals, dark plastics) without looking artificial. Professional product photography HDR."

Example 3 - Subtle HDR Tone Mapping:
"Conservative HDR effect for natural enhancement. Compress tonal range slightly - highlights down 25%, shadows up 20%. Increase midtone contrast by 18% for punch. Add 20% clarity for texture definition. Maintain color saturation - no desaturation from HDR. Avoid the 'HDR look' - keep natural appearance. Result: enhanced detail visibility while maintaining photographic realism."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Balanced approach (Example 1)
- Natural appearance maintained
- Detail visible throughout tonal range
- No harsh halos or artifacts
- Professional and subtle

REQUIREMENTS:
- No over-processing artifacts
- Natural color preservation
- Smooth tonal transitions
- Enhanced detail without looking fake
- Professional photography quality

Generate the instruction.
"""
    },

    26: {
        "id": 26,
        "name": "Noise Reduction / Image Clean-up",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Noise Reduction and Image Quality Cleanup

GOAL: Remove grain, noise, and artifacts while preserving detail

EXAMPLE APPROACHES:

Example 1 - Luminance Noise Reduction:
"Apply noise reduction to smooth grainy areas. Luminance noise: reduce by 60% using edge-aware algorithm - smooth flat areas (plastic housing) while preserving edges and texture details (metal grain, text). Color noise: remove by 75% - eliminate color speckles in shadows and dark areas. Detail preservation: protect edges and fine details like logos, text, mechanical elements. Slight sharpening (12%) after noise reduction to recover edge definition. Result: clean, professional image without looking overly smoothed or 'plastic'."

Example 2 - Selective Area Cleanup:
"Target noise reduction in specific areas. Smooth plastic/painted surfaces: 70% noise reduction. Metal textured areas: 25% reduction to maintain natural texture. Logo/text areas: minimal reduction (10%), maintain sharpness. Shadow areas: 65% reduction to remove color noise. Edge-aware processing prevents detail loss. Follow with selective sharpening: 15% on edges, 5% on smooth areas. Clean result preserving character."

Example 3 - High-ISO Recovery:
"Clean high-ISO sensor noise. Aggressive luminance noise reduction: 75% in smooth areas, 40% in textured areas. Color noise: eliminate 85% (remove color speckles completely). Use surface blur in flat areas while protecting edges. Grain reduction without loss of micro-detail. Sharpening recovery: 18% on product edges. Result: appears shot at low ISO - clean, detailed, professional."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Balanced noise reduction (60% on smooths, 25% on textures)
- Edge-aware processing
- Preserve product detail
- Natural appearance
- Professional cleanup

REQUIREMENTS:
- Noise visibly reduced
- Detail preservation maintained
- No overly smoothed "plastic" look
- Edges remain sharp
- Professional photography quality

Generate the instruction.
"""
    },

    27: {
        "id": 27,
        "name": "Image Upscaling / Super Resolution",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: AI Upscaling to Higher Resolution

GOAL: Increase resolution to HD/4K while adding realistic detail

EXAMPLE UPSCALING:

Example 1 - 4K Upscaling with Detail Generation:
"Upscale image from current resolution to 3840x2160 (4K). Use AI super-resolution to generate realistic micro-detail rather than simple interpolation. In smooth plastic areas: add subtle surface texture and imperfections (0.1mm scale detail). In metal areas: generate realistic grain and machining marks based on visible patterns. Text and logos: sharpen edges to crisp clarity. Prevent noise amplification: apply 12% pre-upscale noise reduction. Post-upscale sharpening: 15% on edges, 8% overall. Result: appears natively shot at 4K resolution."

Example 2 - Detail-Preserving Upscale:
"Double resolution while maintaining quality. Analyze existing textures and patterns to generate plausible higher-resolution detail. Plastic surfaces: add micro-texture consistent with material type. Paint finishes: generate realistic orange-peel texture if glossy. Metal parts: enhance grain structure. Edges: crisp and clean, no jaggies. Color gradients: smooth without banding. Detail generation based on real-world material properties. Natural, not artificial appearance."

Example 3 - Conservative Upscale:
"Upscale to 2X resolution conservatively. Focus on edge refinement - crisp, anti-aliased product outlines. Texture areas: intelligent detail generation matching existing patterns. Smooth areas: clean gradient preservation. Noise/grain: don't amplify - apply light reduction. Sharpening: 12% on edges only. Avoid creating unrealistic patterns or textures. Result: higher resolution maintaining original character and quality."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Upscale to 4K (3840x2160)
- AI detail generation in appropriate areas
- Edge sharpening and refinement
- Natural texture enhancement
- Professional quality output

REQUIREMENTS:
- Resolution significantly increased
- Detail appears natural, not artificial
- No noise amplification
- Edges crisp and clean
- Maintains original quality character

Generate the instruction.
"""
    },

    28: {
        "id": 28,
        "name": "Perspective Correction",
        "category": "All",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: Perspective and Distortion Correction

GOAL: Fix skewed angles, straighten verticals, correct lens distortion

EXAMPLE CORRECTIONS:

Example 1 - Vertical Straightening:
"Correct perspective where product appears to lean backward. Use the product's main vertical element (handle, post, side panel) as reference. Rotate entire image 2.5 degrees clockwise to bring vertical to true perpendicular. Apply perspective correction to eliminate keystoning (top narrower than bottom). Crop 3% from edges to remove gaps created by rotation. Ensure product stands perfectly vertical when viewed. Maintain product proportions - width to height ratio should remain accurate."

Example 2 - Lens Distortion Removal:
"Remove barrel distortion from wide-angle lens. Apply -12 barrel correction value to straighten curved lines. Product edges and straight elements should appear geometrically straight. Wheels should be perfectly circular, not elliptical. Corners should be 90-degree angles if originally designed that way. After correction, crop 2% from edges. Ensure correction doesn't create unnatural appearance - maintain realistic look."

Example 3 - Combined Correction:
"Fix multiple perspective issues. Step 1: Remove barrel distortion (-8 value). Step 2: Straighten vertical alignment (rotate 1.8° counter-clockwise). Step 3: Correct horizontal keystoning (slight perspective warp correction). Step 4: Verify product proportions match real-world dimensions (24\" width to 20\" height ratio). Step 5: Crop minimally to clean edges. Result: product appears correctly photographed with proper perspective."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Analyze and correct obvious perspective issues
- Straighten vertical elements
- Remove visible lens distortion
- Maintain accurate proportions
- Minimal cropping

REQUIREMENTS:
- Product appears correctly aligned
- Geometric accuracy (circles are round, squares are square)
- Natural appearance maintained
- Proportions realistic
- Professional photography perspective

Generate the instruction.
"""
    },

    29: {
        "id": 29,
        "name": "Reflection / Refraction Simulation",
        "category": "Glassware, Jewelry, Electronics",
        "test_image_type": "electronics_laptop",
        "instruction_template": """
OPERATION: Add Realistic Reflections to Glossy/Metallic Surfaces

GOAL: Generate appropriate reflections based on material type

EXAMPLE REFLECTION APPROACHES:

Example 1 - Chrome/Metallic Reflections:
"Add realistic reflections to chrome and metallic surfaces. On curved metallic areas: apply specular highlights at 85% brightness positioned according to light source (top-left). Add environmental reflections: subtle blurred reflections of surroundings (15% opacity) showing on highly polished surfaces. Flat metallic areas: sharper environmental reflections (25% opacity). Reflections should follow surface curvature - compressed on tight curves, elongated on gradual curves. Color tint: slight blue shift for chrome (RGB: 200,205,210)."

Example 2 - Glossy Plastic Reflections:
"Apply appropriate reflections for glossy plastic surfaces. Specular highlights: medium intensity (60% brightness) positioned according to lighting. Environmental reflections: very subtle (8-12% opacity), soft blur (5px). Reflections more visible on darker plastic areas. Maintain plastic's base color while adding realistic gloss appearance. Highlights should be white-neutral, not colored. Surface curve determines highlight shape - oval on rounded areas, linear on edges."

Example 3 - Glass/Transparent Surface:
"Generate glass-like reflections and refractions. Surface reflections: 30% opacity showing environment. Specular highlights: sharp and bright (90% brightness) at light contact points. Refraction: slight distortion of elements visible through glass (if applicable). Fresnel effect: stronger reflections at glancing angles, weaker head-on. Transparent areas show background with slight color tint from glass. Realistic glass material properties."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Analyze material type and apply appropriate reflections
- Metal: high specular, environmental reflections
- Plastic: moderate specular, minimal environmental
- Natural appearance for material type
- Professional product photography

REQUIREMENTS:
- Reflections match material properties
- Light direction consistent
- Natural and realistic appearance
- Enhances product without looking artificial
- Professional photography quality

Generate the instruction.
"""
    },

    30: {
        "id": 30,
        "name": "Texture Mapping for 3D / AR",
        "category": "Tools, Industrial, Electronics",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Generate Normal/Displacement Maps for 3D Applications

GOAL: Create technical texture maps for AR/VR/3D modeling use

EXAMPLE MAP GENERATION:

Example 1 - Normal Map Creation:
"Generate a normal map showing surface micro-detail. Analyze visible textures and convert to RGB normal map format: Red channel represents X-axis (horizontal) surface angles, Green channel represents Y-axis (vertical) angles, Blue channel represents Z-axis (height/depth). Flat surfaces appear neutral purple/blue (RGB: 128,128,255). Raised details (bolts, badges) appear lighter/pink tones. Recessed details (grooves, panel gaps) appear darker/blue tones. Capture detail at 1mm resolution. Standard tangent-space normal map suitable for 3D rendering engines."

Example 2 - Displacement Map:
"Create grayscale displacement/height map. White (RGB: 255,255,255) represents highest points (bolt heads, raised logos, top surfaces). Black (RGB: 0,0,0) represents lowest points (screw holes, deep grooves, recesses). Grey values represent intermediate heights. Smooth gradients between height transitions. Dynamic range: 8mm maximum height variation mapped across full 0-255 range. Suitable for 3D mesh displacement in AR applications. Clean, anti-aliased edges."

Example 3 - Combined PBR Texture Set:
"Generate complete PBR (Physically Based Rendering) texture set. 1) Albedo/Diffuse map: pure color without lighting (remove all shadows and highlights). 2) Normal map: surface detail (as Example 1). 3) Roughness map: white for rough areas (rubber grips), black for glossy areas (chrome parts). 4) Metallic map: white for metal, black for non-metal. All maps 4K resolution (4096x4096), aligned perfectly. Suitable for game engines and AR frameworks."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Generate standard normal map (Example 1)
- Tangent-space format
- High resolution (2K or 4K)
- Industry-standard RGB encoding
- Clean, usable for 3D/AR pipelines

REQUIREMENTS:
- Technically accurate map format
- Appropriate resolution for AR use
- Proper color space encoding
- Clean, artifact-free
- Industry-standard compatibility

Generate the instruction.
"""
    },

    31: {
        "id": 31,
        "name": "Annotation & Feature Overlay",
        "category": "Electronics, Tools, Plumbing, Industrial",
        "test_image_type": "electronics_laptop",
        "instruction_template": """
OPERATION: Professional Product Part Annotation & Callouts

GOAL: Create clear, professional, and unambiguous callouts to label specific product parts for technical documentation, user manuals, or e-commerce listings.

THE ONE-LINE, ONE-LABEL RULE (ABSOLUTE):
This is the most critical rule to prevent clutter and confusion.
1. Each labeled part gets EXACTLY ONE callout line originating from it.
2. Each callout line connects to EXACTLY ONE text label.
3. Callout lines MUST NOT cross each other or other components.
4. Do NOT use numbers, unless the user specifically requests a numbered list. The direct line-to-label connection is clearer.

CALLOUT GEOMETRY SPECIFICATIONS (for a professional look):

1. The Anchor Dot:
   - Placement: Place a small, solid circle (3-5px diameter) DIRECTLY ON the surface of the component being labeled.
   - Color: Use a high-contrast color (e.g., white dot on a dark part, dark gray dot on a light part).
   - Purpose: This is the precise origin point of the callout.

2. The Callout Line (Dog-Leg Style):
   - This line should have two segments (an "elbow") for professional organization.
   - Segment 1 (Angled): Starts from the Anchor Dot and extends outwards at a clean angle (e.g., 30, 45, or 60 degrees) away from the product's main body.
   - Segment 2 (Horizontal): At the end of the angled segment, it turns to become perfectly horizontal, extending to the text label.
   - Style: 1-2px solid line, same color as the Anchor Dot.
   - Purpose: This structure ensures all text labels can be aligned neatly in a column.

3. The Text Label:
   - Content: Clearly state the name of the part (e.g., "USB-C 3.2 Port", "Power Button", "Air Intake Vent").
   - Font: Use a clean, readable sans-serif font like Arial or Helvetica.
   - Size: 12-14pt.
   - Color: High contrast with the background.
   - Positioning: Text begins at the end of the horizontal callout line segment.

LAYOUT & COMPOSITION RULES:

- Organize Labels in Columns: All text labels should be aligned vertically in one or two columns in the negative space to the LEFT or RIGHT of the product. Do not scatter labels randomly around the image.
- Consistent Alignment: All text within a column should be left-aligned (if labels are on the right) or right-aligned (if labels are on the left). This creates a clean, organized "table of contents" look.
- Even Spacing: Maintain consistent vertical spacing between each text label in a column.
- Avoid Obstruction: Plan the angles of the callout lines so they do not cross over important product details. The path from dot to label should be clear.

INTELLIGENT PART IDENTIFICATION (if user does not specify):
Analyze the product image and identify 3-5 of the most important VISIBLE, EXTERNAL parts to label. Prioritize:
1. User Interaction Points: Buttons, switches, knobs, screens, charging ports.
2. Key Functional Components: Lenses, sensors, blades, motors, vents, connection points.
3. Branding & Model Names: The primary brand logo, model number text.
4. Material Callouts: If a specific part is made of a premium material (e.g., "Carbon Fiber Frame", "Titanium Housing").

EXAMPLE APPROACH (for a Laptop):

"Analyze: The product is a laptop. Key external parts include: USB-C ports, USB-A port, HDMI port, power button, trackpad, and keyboard.

COMPOSITION PLAN:
- Place all text labels in a neat column on the right side of the image.
- All text will be left-aligned.
- Callout lines will be dog-leg style, extending from the parts to the labels.

EXECUTION INSTRUCTIONS:

1. Label 'USB-C Port':
   - Place a 4px white solid dot directly on the leftmost USB-C port.
   - From this dot, draw a 2px white line at a 45-degree angle upwards and to the right.
   - After extending 2 inches, turn the line to be perfectly horizontal, extending another 3 inches to the right margin.
   - At the end of the line, add the text 'USB-C / Thunderbolt 4 Port' in Arial, 13pt, white.

2. Label 'HDMI Port':
   - Place a 4px white dot directly on the HDMI port.
   - Draw a 2px white line horizontally to the right.
   - After extending 1.5 inches, turn the line 45-degrees upwards, extending another 2 inches to align horizontally with the label text above it.
   - At the end of the line, add the text 'HDMI 2.1 Output' in Arial, 13pt, white. Ensure this label is vertically aligned below the first label with 1-inch spacing.

3. Label 'Power Button':
   - Place a 4px white dot on the power button, which is separate from the keyboard.
   - Draw a 2px white line at a 60-degree angle upwards and to the right.
   - Extend until it is horizontally aligned with the third label position in the column.
   - At the end of the line, add the text 'Power Button / Fingerprint Reader' in Arial, 13pt, white.

...Continue for all identified parts, ensuring all labels are neatly aligned in the right-hand column and all connection lines are clean and do not cross. The laptop itself must remain completely unchanged beneath these vector overlays. The final image should look like a professional page from a high-end user manual."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS PROVIDED:
- Intelligently identify 3-5 key external parts using the priority list above.
- Use the direct dot-to-line-to-label system.
- Organize all labels into a single, clean column on either the left or right side.

PROFESSIONAL STANDARDS CHECKLIST:
- ✓ Is the ONE-LINE, ONE-LABEL rule followed for every callout?
- ✓ Are all callout lines clean, non-crossing, and easy to follow?
- ✓ Are all text labels neatly aligned in a column?
- ✓ Is the font clean, readable, and professional?
- ✓ Is there high contrast between the callout graphics and the image?
- ✓ Is the product completely untouched beneath the overlays?
- ✓ Is the final image clear, professional, and unambiguous?

NEVER DO:
- Draw more than one line from a single part or to a single label.
- Allow callout lines to cross each other.
- Scatter labels randomly around the image.
- Use numbering unless specifically requested by the user.
- Place labels where they are hard to read or ambiguous.
- Obscure any part of the product with text or lines.

NOTE: The examples are for reference and you are not restricted to be imaginative(but professional)
Generate a hyper-specific instruction for Nano Banana to create a professional and clean annotation overlay.
"""
    },

    32: {
        "id": 32,
        "name": "Infographic / Data Overlay",
        "category": "Tools, Electronics, Industrial",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Specifications and Data Visualization Overlay

GOAL: Add product specifications as visual infographic elements

EXAMPLE INFOGRAPHIC STYLES:

Example 1 - Spec Panel:
"Create professional specification panel overlaid on image. Panel design: rounded rectangle (380px wide, auto height based on content) positioned in top-right corner with 40px margin from edges. Background: dark grey (RGB: 45,45,50) at 90% opacity with subtle gradient. Border: 2px white at 15% opacity. Content layout vertically with icon + text pairs:
  ⚡ Power: 60V Lithium (icon + white Arial Bold 15pt)
  📏 Width: 24 inches
  📐 Height: 20 inches  
  ⚖ Weight: 95 lbs
  🔋 Battery: 10.0Ah
Use simple white icons (18px) left-aligned, text with 10px left padding. 18px vertical spacing between rows. 20px padding all sides of panel. Professional data sheet aesthetic."

Example 2 - Circular Info Graphics:
"Create circular stat graphics. Design 3-4 circular badges (80px diameter) arranged along top edge of image. Each badge: colored ring (4px width) at 60% filled (suggesting capability), center shows icon + value. Colors: blue #0078D4 (power), green #10B981 (eco), orange #F59E0B (performance). Inside circle: small icon above numerical value (white text, Arial Bold 16pt) with label below (11pt). Semi-transparent dark background (75% opacity) behind each badge. Modern, dashboard-style presentation."

Example 3 - Side Bar Stats:
"Vertical specification bar along left edge. Bar: 120px wide, full height, gradient from dark grey top (RGB: 50,50,55) to slightly lighter bottom (RGB: 60,60,65), 85% opacity. Content: stacked spec items with divider lines between. Each item: label (white Arial 11pt, 70% opacity) above value (white Arial Bold 18pt, 100% opacity). Small colored accent bars (3px wide) left of each item in different colors. 25px padding, 35px spacing between items. Sleek, modern product sheet design."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Spec panel approach (Example 1)
- Include 4-6 key specifications
- Professional, readable design
- Positioned to not obscure product
- Clean, modern aesthetic

REQUIREMENTS:
- Text clearly readable (minimum 11pt for labels, 14pt for values)
- Panel doesn't cover important product features
- Professional graphic design
- Data organized logically
- Modern, appealing visual design

Generate the instruction.
"""
    },

    33: {
        "id": 33,
        "name": "Multi-Product Composite Layout",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Arrange Multiple Products in Composite Image

GOAL: Create professional layout showing multiple SKUs or product variants together

EXAMPLE LAYOUTS:

Example 1 - Grid Arrangement:
"Create 2x2 grid layout showing this product plus 3 variants/accessories. Main product (this image): top-left position, full size. Accessories: battery (top-right, 60% scale), extension chute (bottom-left, 60% scale), cover bag (bottom-right, 60% scale). All items on same baseline/ground plane. Consistent lighting (all from top-left). Each product has matching drop shadow (40% opacity, 18px blur, 5px offset). 4-inch spacing between products. All products in sharp focus. Clean white background. Professional product family presentation."

Example 2 - Hero + Supporting Layout:
"Hero product (this image) occupies left 60% of frame, positioned center-left. Three supporting products arranged vertically on right 35%: top accessory at 35% scale, middle accessory at 35% scale, bottom accessory at 35% scale. Vertical spacing: 2 inches between items. All aligned right edge. Hero maintains full detail and focus, supporting products equally detailed but smaller. Same lighting direction across all products. Unified shadows. Professional catalog layout."

Example 3 - Linear Showcase:
"Arrange 4-5 product variants in horizontal line. This product as base reference, then show color variants or configuration options. Each product: same scale, evenly spaced (3 inches between), on shared ground plane. Lighting and shadows consistent across all. Slight perspective gradient - items further right subtly smaller (95% → 90% scale) for depth. All products maintain clarity and detail. Professional comparison layout showing options."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Grid arrangement if multiple distinct products
- Hero + supporting if showing main product with accessories
- Consistent lighting and shadows
- Professional spacing and alignment
- Clear, organized presentation

REQUIREMENTS:
- All products properly scaled and proportioned
- Consistent lighting across items
- Clean alignment and spacing
- Professional composition
- All products clearly visible

Generate the instruction.
"""
    },

    34: {
        "id": 34,
        "name": "Virtual Staging / Scene Generation",
        "category": "Furniture, Industrial, Tools",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Multi-Product Virtual Environment Staging

GOAL: Place multiple products in realistic virtual space (room, workshop, warehouse)

EXAMPLE STAGING:

Example 1 - Workshop Scene:
"Create residential garage workshop scene with this product and related tools. Setting: grey epoxy floor, white walls with pegboard section showing tools (blurred). Main product: positioned on workbench center-left at 45-degree angle, sharp focus. Supporting items (blurred 10px): red toolbox background-right, orange extension cord foreground-right, small hand tools on bench. Overhead LED shop lighting (5000K) creating realistic shadows. Camera at 4-foot height slight downward angle. Products maintain sharp focus, environment provides context at reduced clarity. Professional workshop photography."

Example 2 - Warehouse/Storage Setting:
"Industrial warehouse environment. Products arranged on metal shelving unit (2-shelf visible). This product on middle shelf center, two similar units flanking at 70% blur. Concrete floor visible below, industrial ceiling hints above (heavy blur). Metal shelf in sharp focus immediately around products. Fluorescent warehouse lighting (4500K) from above. Products well-lit, environment darker (reduced 25%). Depth through selective focus - sharp shelves, blurred far background. Professional industrial catalog photography."

Example 3 - Retail Display:
"Showroom floor display setting. This product on display pedestal (white, clean), positioned center-stage. Surrounding context: other products on nearby displays (12px blur), retail signage hints in background (heavily blurred), clean floor reflecting overhead track lighting. Bright, professional retail lighting (5000K). Product in perfect focus with studio-quality lighting, environment supports context without competing. Upscale retail presentation."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Choose contextually appropriate environment
- Product(s) in sharp focus
- Environment at 8-12px blur for context
- Professional lighting matching environment type
- Realistic spatial arrangement

REQUIREMENTS:
- Products maintain sharp focus and detail
- Environment enhances without distracting
- Realistic lighting for setting type
- Proper scale and spatial relationships
- Professional photography quality

Generate the instruction.
"""
    },

    35: {
        "id": 35,
        "name": "Product Wear / Usage Simulation",
        "category": "Tools, Industrial, Automotive",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Simulate Product Wear, Aging, or In-Use Condition

GOAL: Show realistic wear patterns or aged appearance

EXAMPLE WEAR SIMULATIONS:

Example 1 - Light Use Wear:
"Apply realistic light-use wear patterns. Handle areas: add 8-12 small scratches (0.5-2 inches long, subtle grey showing through red paint) where hands grip frequently. Front edge of housing: add 3-5 small paint chips (0.25-inch diameter) exposing grey primer beneath. Wheels: slight scuff marks on outer edges (darker grey streaks). Dust/dirt accumulation: very light brown/grey (8% opacity) in crevices around wheels and base. Auger blades: minor surface scratches, no rust. Overall: 85% pristine, 15% showing normal use. Realistic, not damaged appearance."

Example 2 - Moderate Wear:
"Simulate moderate outdoor tool use. Handle grips: worn smooth in contact areas, slight color fading (15% lighter). Housing: 15-20 paint chips various sizes (0.2-0.5 inches), concentrated on corners and edges. Metal components: light surface rust spots (orange-brown, small 0.3-inch spots, 5-8 total) on auger blades and bolts. Dirt accumulation: brown/grey in all crevices and seams (15-20% opacity). Logos slightly faded (10% transparency increase). Wheels show wear - tread slightly worn. Overall: well-used but maintained tool appearance."

Example 3 - Aged/Vintage Appearance:
"Create aged, well-worn vintage look. Paint: faded 25% lighter overall, multiple chips and scratches exposing metal (20-30 instances). Metal parts: patina and oxidation - not shiny, slightly dulled. Surface rust: moderate (orange-brown areas on exposed metal, 30-40% coverage on older steel parts). Wear concentrated on high-use areas: handles very worn, edges chipped heavily. Dirt and grime: accumulated in all recesses (25% opacity brown/grey). Maintains structural integrity but shows age. Vintage equipment aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Light use wear (Example 1)
- Realistic, not damaged
- Wear in logical high-contact areas
- Maintains product recognizability
- Professional aging simulation

REQUIREMENTS:
- Wear patterns realistic and logical
- Product still identifiable
- Age/wear level appropriate for context
- Natural appearance, not artificially distressed
- Professional simulation quality

Generate the instruction.
"""
    },

    36: {
        "id": 36,
        "name": "Seasonal / Thematic Contexts",
        "category": "B2C Retail, Apparel, Furniture",
        "test_image_type": "furniture_chair",
        "instruction_template": """
OPERATION: Add Seasonal or Holiday Thematic Elements

GOAL: Create seasonal context (holiday, summer, winter themes) around product

EXAMPLE SEASONAL THEMES:

Example 1 - Winter Holiday:
"Apply subtle winter holiday theme. Background: replace with snowy residential driveway scene - snow-covered ground, house with white string lights along eaves (soft glow), light snowfall (delicate white flakes, semi-transparent, various sizes falling). Product: light snow dusting on top surfaces (thin white layer, natural accumulation pattern). Small decorative element: red velvet bow on product handle (tasteful, not overwhelming). Color grading: cool winter tones - slight blue shift (color temp 6500K). Maintain product clarity and professionalism. Festive but sophisticated, not overly decorated."

Example 2 - Summer Outdoor:
"Create summer outdoor theme. Background: sunny backyard setting - green grass (slightly out of focus), wooden fence in background, clear blue sky, bright natural sunlight. Product positioned as if ready for summer use. Surrounding elements: hint of patio furniture in blurred background, perhaps garden hose or potted plants. Warm color grading - slight yellow/warm shift (6200K). Bright, cheerful lighting. Product remains main focus in sharp detail. Summer lifestyle context without cluttering."

Example 3 - Autumn/Fall:
"Apply autumn theme. Background: fallen leaves scattered on ground around product (orange, yellow, brown leaves, realistic distribution). Background hints: trees with autumn foliage (heavily blurred), perhaps pumpkins or hay bale in far background (subtle, not dominant). Warm color grading - golden hour lighting feel (5800K warm). Soft shadows suggesting late afternoon sun. Product sharp and clear, seasonal elements provide context. Professional autumn catalog photography aesthetic."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Choose seasonally appropriate theme if obvious (snow blower → winter)
- Subtle, professional execution
- Product remains primary focus
- Context enhances without overwhelming
- Tasteful, not over-decorated

REQUIREMENTS:
- Product clearly visible and unchanged at core
- Seasonal elements appropriate and tasteful
- Professional photography quality
- Not cartoonish or over-done
- Enhances product appeal

Generate the instruction.
"""
    },

    37: {
        "id": 37,
        "name": "AI-Generated Artistic Variants",
        "category": "All",
        "test_image_type": "product_tool",
        "instruction_template": """
OPERATION: Create Stylized Social Media or Artistic Versions

GOAL: Generate eye-catching stylized variants for social media, ads, marketing

EXAMPLE ARTISTIC STYLES:

Example 1 - Bold Gradient Background:
"Create Instagram-ready artistic variant. Product: render in clean illustrated style with defined edges and enhanced colors (increase saturation by 35%, boost contrast by 25%). Background: vibrant gradient from electric blue top-left (Hex: #0066FF) to deep purple bottom-right (Hex: #8B00FF). Add subtle white glow around product edges (20% opacity, 25px soft blur) for separation. Include minimal geometric elements: 2-3 semi-transparent white circles (various sizes, 10% opacity) scattered in background. Modern, energetic social media aesthetic. Square format 1:1 for Instagram."

Example 2 - Minimalist Line Art:
"Transform into minimalist graphic variant. Product: outlined with clean vector-style edges (3px white stroke with dark outline), some internal detail lines showing key features. Fill: solid color blocks maintaining product's color zones. Background: single solid color (choose complementary - if product is red, use deep teal Hex: #006B7D). Add small text element: product name in modern sans-serif font (white, 24pt, bottom corner). Flat design aesthetic, suitable for modern ads and social posts."

Example 3 - Dramatic Spotlight Style:
"Create dramatic artistic version. Background: dark gradient (deep charcoal RGB: 35,35,40 to black). Product: enhanced with strong edge lighting - bright white rim lights on contours (85% intensity) as if dramatically lit in studio. Main product colors slightly desaturated (15% reduction) for moody aesthetic. Add subtle lens flare effect from top-left (star-burst, 40% opacity). Cinematic, high-impact look for premium marketing materials. Dramatic and eye-catching."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Bold gradient approach (Example 1)
- Instagram square format (1:1)
- Modern, vibrant aesthetic
- Product clearly recognizable
- Social media optimized

REQUIREMENTS:
- Product remains recognizable
- Stylized but professional
- Appropriate for marketing use
- Eye-catching and modern
- Platform-optimized format

Generate the instruction.
"""
    },
    
    38: {
        "id": 38,
        "name": "Watermark / Branding Overlay",
        "category": "All",
        "test_image_type": "beauty_bottle",
        "instruction_template": """
OPERATION: Add Watermark or Branding

GOAL: Add logos, watermarks, or brand marks subtly

EXAMPLE PLACEMENTS:

Example 1 - Corner Logo:
"Add logo in bottom-right corner. Position 40px from right edge, 40px from bottom edge. Scale logo to 10% of image width. Set opacity to 60% for subtle presence. Add subtle drop shadow: black at 25% opacity, 4px blur, 2px offset down and right. Logo should be visible but not dominate the product."

Example 2 - Watermark with Text:
"Place semi-transparent watermark across bottom third of image. Text: '[Brand Name]' in white Arial Bold 24pt at 45% opacity. Position centered horizontally, 15% from bottom. Add subtle black outline (1px) for visibility on any background. Ensure it doesn't obscure product features."

Example 3 - Minimal Brand Mark:
"Add small brand icon in top-left corner at 8% of image width. Position 30px from edges. Render in white at 55% opacity with 3px soft shadow (black, 20% opacity). Extremely subtle, professional watermarking."

USER SPECIFICATIONS:
{user_details}

IF NO USER DETAILS:
- Bottom-right corner placement
- 8-10% of image width
- 50-60% opacity
- Subtle drop shadow for visibility
- Doesn't obscure product

REQUIREMENTS:
- Watermark subtle but visible
- Doesn't damage product presentation
- Professional appearance
- Proper positioning and scaling

Generate the instruction.
"""
},
    39: {
        "id": 39,
        "name": "Studio backdrop",
        "category": "All",
        "test_image_type": "none",
        "instruction_template": """
OPERATION: Create studio/solid background based on provided input product image.

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
}
}

# ===========================
# HELPER FUNCTIONS
# ===========================

def get_operation_by_id(operation_id):
    """Get operation config by ID"""
    return OPERATIONS.get(int(operation_id))

def get_all_operation_ids():
    """Get list of all operation IDs"""
    return list(OPERATIONS.keys())

def get_operation_template(operation_id, user_details=""):
    """Get formatted template with user details inserted"""
    op = get_operation_by_id(operation_id)
    if not op:
        return None
    
    template = op["instruction_template"]
    
    # Insert user details or mark as not provided
    if user_details and user_details.strip():
        template = template.replace("{user_details}", user_details)
    else:
        template = template.replace("{user_details}", "None provided - use default approach")
    
    return template

def get_test_image_type(operation_id):
    """Get the image type needed for testing this operation"""
    op = get_operation_by_id(operation_id)
    return op.get("test_image_type", "product_generic") if op else "product_generic"