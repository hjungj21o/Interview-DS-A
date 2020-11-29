1. Hoopsbnb - Functional Airbnb Clone that lets users rent out basketball courts
    -- Tech stacks: Ruby on Rails, React/Redux
    -- Pros:
        --- A lot of firsts:
            1. First time having full creative reigns without any instructional boundaries
            2. First time using exernal APIs like Google Maps API
            3. First full stack project that allowed me to really piece everything I learned together
    -- What I would do differently:
        --- Modularize the code a bit more - login/signup is separated by a ternary
        --- Be more organized in how I code via wireframes etc. - Felt like I just put on blinders and kept running until the finish line
    --Trouble point:
        --- When I searched something, the map wouldn't update. So I manually set some coordinates, added the keyword to the UI slice of state (which would
            trigger a rerender) and made the map move, which would fetch the right lists and markers. 
    -- Rails ActiveRecord Query:
        Find lat/long boundaries in Maps API to fetch markers - when the boundaries change, it gets arenas that are within those bounds
        Search - use ILIKE search to find a close match of keywords of location (BK, Manhattan, etc.)
    -- React vs Angular vs Vue
        -- Multiple reasons, easiest being it was a part of my assignment but would have still chosen React, for a number of reasons:
        -- Marketability:
            -- React is probably the most in-demand right now
            -- Vue fell short here as well because the documentation as well as the community isn't as robust as Angular/React
        -- Performance:
            -- Angular is too big as it's an entire framework, whereas Vue and React are smaller libraries
            -- React is in the middle in terms of startup performance, Vue is slightly quicker but again, less marketability
            

2. Zoe - A personal assistant web app that provides weekly meal plans based on health goals
    -- Used the MERN stack - had to learn Node.js and MongoDB in 5 days and build something
    -- First group project, I served as a flex engineer, jumping in both front and backend to alleviate bottlenecks
    -- Built a multi-form sign up page:
        Challenge was when toggling back and forth, it would lose all the progress.
        Solution: Save the data to UI state, then when we go back or forward, rerender with all the state information.
    -- Pros:
        -- First time designating and doing a group project, which meant that we could focus on one or two features
        -- Learned a new tech stack and utilized it in a matter of days
    -- Different:
        -- Just wish there was more time. 
        -- Wish commented/documented a lot of the coebase b/c when jumping in to help, I had to buckle down and try to understand what others wrote

3. DigiDex - An interactive business card web app that complements physical business cards
    -- Vanilla JS
    -- Used canvas to create a card with floating circles

4. The Giving Grape - A non-profit organization where I'm volunteering at, working on the web app
    -- Wanted to move the verification process in-house instead of using Twiliio b/c it was getting too costly
    -- Created a new column on the users table to save user's unique verification code
    -- Created a function that generates a 6 digit numerical code which then gets sent to the user's email
        -- User's input is then matched with the database
    -- Also created a sleep method which waits 10 minutes for the input to be matched.
        -- If it goes over 10 minutes, the verification code in database becomes nil
        -- Will prompt the user to ask for the verification code again

    -- It's my favorite project b/c not only do my codes have an actual business impact,
        -- it's code that's actually helping real life users
        -- and I'm constantly learning new things from my fellow volunteers and practicing reading/understanding their way of writing code.
