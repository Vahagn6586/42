/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/06 15:24:37 by vchiling          #+#    #+#             */
/*   Updated: 2026/04/21 18:37:15 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

/*
• %c Prints a single character. (ft_putchar.c)
• %s Prints a string (as defined by the common C convention). (ft_putstr.c)
• %p The void * pointer argument has to be printed in hexadecimal format. ()
• %d Prints a decimal (base 10) number. (ft_itoa_base.c)
• %i Prints an integer in base 10. (ft_itoa_base.c)
• %u Prints an unsigned decimal (base 10) number. (ft_itoa_base.c)
• %x Prints a number in hexadecimal (base 16) lowercase format. (ft_itoa_base.c)
• %X Prints a number in hexadecimal (base 16) uppercase format. (ft_itoa_base.c)
• %% Prints a percent sign. (ft_putchar.c)
*/

void	normalize_flags(int *flags, int precision, char spec)
{
	if (*flags & F_MINUS)
		*flags &= ~F_ZERO;
	if (*flags & F_PLUS)
		*flags &= F_SPACE;
	if (precision >= 0 && ft_strchr(IS_INT, spec))
		*flags &= ~F_ZERO;
	if ((*flags & F_HASH) && (spec != 'x' || spec != 'X'))
		*flags &= ~F_HASH;
}

void	fill_struct(t_fspec *specs)
{
	specs[0] = (t_fspec){'c', handle_c};
	specs[1] = (t_fspec){'s', handle_s};
	specs[2] = (t_fspec){'p', handle_p};
	specs[3] = (t_fspec){'d', handle_i_d};
	specs[4] = (t_fspec){'i', handle_i_d};
	specs[5] = (t_fspec){'u', handle_u};
	specs[6] = (t_fspec){'x', handle_x};
	specs[7] = (t_fspec){'X', handle_X};
	specs[8] = (t_fspec){'%', handle_percent};
}

void	specifier_check(va_list *args, const char format, t_fspec *specs,
		int *ret_val)
{
	int	j;

	j = 0;
	while (specs[j].fspec)
	{
		if (format == specs[j].fspec)
		{
			*ret_val += specs[j].handler(args);
			break ;
		}
		++j;
	}
}

int	scanner(va_list *args, const char *format, t_fspec *specs)
{
	int	i;
	int	ret_val;

	i = 0;
	ret_val = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			++i;
			if (!format[i])
				break ;
			specifier_check(args, format[i], specs, &ret_val);
		}
		else
		{
			write(1, &format[i], 1);
			++ret_val;
		}
		++i;
	}
	return (ret_val);
}

int	ft_printf(const char *format, ...)
{
	va_list	args;
	t_fspec	specs[10];
	int		flags;
	int		bite_count;

	fill_struct(specs);
	va_start(args, format);
	bite_count = scanner(&args, format, specs);
	va_end(args);
	return (bite_count);
}
