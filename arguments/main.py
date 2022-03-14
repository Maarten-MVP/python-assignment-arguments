# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, template=f'Hello, <name>!'):
    if template == 'Hello, <name>!':
        return(f'Hello, {name}!')
    else:
        greet = template.replace('<name>', name)
        return(greet)
        

def force(mass, body='earth'):
    gravities = {
        'sun': 274,
        'jupiter': round(24.92, 1),
        'neptune': round(11.15,1),
        'saturn': round(10.44,1),
        'earth': round(9.798,1),
        'uranus': round(8.87,1),
        'venus': round(8.87,1),
        'mars': round(3.71,1),
        'mercury': round(3.7,1),
        'moon': round(1.62,1),
        'pluto': round(0.58,1)
    }
    force = mass * gravities[body]
    return(force)


def pull(m1, m2, d):
    pull = (6.674 * 10 ** -11) * ((m1 * m2)/d ** 2)
    return(pull)

pull(800, 1500, 3)

